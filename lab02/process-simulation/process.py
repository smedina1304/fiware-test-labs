#
# Classe: ProcessSimulation
#

# [START import_module]
import time
import random

import paho.mqtt.client as paho

from datetime import datetime
from elements.tank import Tank
from elements.valve import Valve
from elements.pump import Pump
from elements.cooler import Cooler
# [END import_module]

# [START - Class]
class ProcessSimulation():
    """
    ### Classe: ProcessSimulation

    Classe de simulação do processo.
    
    by Sérgio C. Medina
    """

    # [METHOD - Constrution]
    def __init__(self,mqtt_client=None, mqtt_prefix=None, sleepTime=5, debugLevel=0):

        # MQTT
        self.mqtt_client = mqtt_client
        self.mqtt_prefix = mqtt_prefix
        self.sleepTime = sleepTime
        self.__debug = debugLevel
        
        # Tanks
        self.__tank_1 = Tank()
        self.__tank_1.setAttribute(id='NAME' , value='TQ1')
        self.__tank_1.setAttribute(id='LEVEL.HIGH' , value=90)
        self.__tank_1.setAttribute(id='LEVEL.LOW' , value=10)
        self.__tank_1.setAttribute(id='TEMP.HIGH' , value=42)
        self.__tank_1.setAttribute(id='TEMP.LOW' , value=35)        
        self.__tank_1.setAttribute(id='CAPACITY' , value=35000)
        self.__tank_1.setAttribute(id='CAPACITY.UNIT' , value='LT')

        self.__tank_2 = Tank()
        self.__tank_2.setAttribute(id='NAME' , value='TQ2')
        self.__tank_2.setAttribute(id='LEVEL.HIGH' , value=90)
        self.__tank_2.setAttribute(id='LEVEL.LOW' , value=10)
        self.__tank_2.setAttribute(id='TEMP.HIGH' , value=30)
        self.__tank_2.setAttribute(id='TEMP.LOW' , value=20)        
        self.__tank_2.setAttribute(id='CAPACITY' , value=40000)
        self.__tank_2.setAttribute(id='CAPACITY.UNIT' , value='LT')
        
        self.__tank_3 = Tank()
        self.__tank_3.setAttribute(id='NAME' , value='TQ3')
        self.__tank_3.setAttribute(id='LEVEL.HIGH' , value=90)
        self.__tank_3.setAttribute(id='LEVEL.LOW' , value=10)
        self.__tank_2.setAttribute(id='TEMP.HIGH' , value=40)
        self.__tank_2.setAttribute(id='TEMP.LOW' , value=20)        
        self.__tank_3.setAttribute(id='CAPACITY' , value=60000)
        self.__tank_3.setAttribute(id='CAPACITY.UNIT' , value='LT')


        # Valve
        self.__valve_1_IN = Valve()
        self.__valve_1_IN.setAttribute(id='NAME' , value='VALVE.1.IN')
        self.__valve_1_RET= Valve()
        self.__valve_1_RET.setAttribute(id='NAME' , value='VALVE.1.RET')
        self.__valve_1_OUT= Valve()
        self.__valve_1_OUT.setAttribute(id='NAME' , value='VALVE.1.OUT')

        self.__valve_2_IN = Valve()
        self.__valve_2_IN.setAttribute(id='NAME' , value='VALVE.2.IN')
        self.__valve_2_RET= Valve()
        self.__valve_2_RET.setAttribute(id='NAME' , value='VALVE.2.RET')
        self.__valve_2_OUT= Valve()
        self.__valve_2_OUT.setAttribute(id='NAME' , value='VALVE.2.OUT')

        self.__valve_3_OUT= Valve()
        self.__valve_3_OUT.setAttribute(id='NAME' , value='VALVE.3.OUT')

        # Pump
        self.__pump_1 = Pump()
        self.__pump_1.setAttribute(id='NAME' , value='PUMP1')
        self.__pump_2 = Pump()
        self.__pump_2.setAttribute(id='NAME' , value='PUMP2')
        self.__pump_3 = Pump()
        self.__pump_3.setAttribute(id='NAME' , value='PUMP3')

        # Cooler
        self.__cooler_1 = Cooler()
        self.__cooler_1.setAttribute(id='NAME' , value='COOLER1')

        self.__cooler_2 = Cooler()
        self.__cooler_2.setAttribute(id='NAME' , value='COOLER2')

        # Ciclos de process
        self.__ciclosTqAvaliables = 0
        self.__ciclosTqAvaliablesMax = 100
        self.__ciclosTqFill = 0
        self.__ciclosTqFillMax = 30
        self.__ciclosTqColl = 0
        self.__ciclosTqCollMax = 20        


    def simulationLogic(self):

        # TANK 1
        for tk in [self.__tank_1, self.__tank_2]:
            self.simulationTankBuffer(tk)
            sentData = tk.publishMQTT(self.mqtt_client, self.mqtt_prefix)
            if self.__debug>=2:
                print('## MQTT', tk.getAttribute(id='NAME'), ':\n', sentData, '\n')

            time.sleep(self.sleepTime/5)

        # COOLER
        for cl in [self.__cooler_1, self.__cooler_2]:
            sentData = cl.publishMQTT(self.mqtt_client, self.mqtt_prefix)
            if self.__debug>=2:
                print('## MQTT', cl.getAttribute(id='NAME'), ":\n", sentData)

            time.sleep(self.sleepTime/5)

        # VALVES
        for valve_IN in [self.__valve_1_IN, self.__valve_2_IN]:
            sentData = valve_IN.publishMQTT(self.mqtt_client, self.mqtt_prefix)
            if self.__debug>=2:
                print('## MQTT', valve_IN.getAttribute(id='NAME'), ":\n", sentData)

        time.sleep(self.sleepTime/5)

        for valve_RET in [self.__valve_1_RET, self.__valve_2_RET]:
            sentData = valve_RET.publishMQTT(self.mqtt_client, self.mqtt_prefix)
            if self.__debug>=2:
                print('## MQTT', valve_RET.getAttribute(id='NAME'), ":\n", sentData)

        time.sleep(self.sleepTime/5)

        for valve_OUT in [self.__valve_1_OUT, self.__valve_2_OUT]:
            sentData = valve_OUT.publishMQTT(self.mqtt_client, self.mqtt_prefix)
            if self.__debug>=2:
                print('## MQTT', valve_OUT.getAttribute(id='NAME'), ":\n", sentData)

        time.sleep(self.sleepTime/5)

        # PUMPS
        for pump in [self.__pump_1, self.__pump_2]:
            sentData = pump.publishMQTT(self.mqtt_client, self.mqtt_prefix)
            if self.__debug>=2:
                print('## MQTT', pump.getAttribute(id='NAME'), ":\n", sentData)

        time.sleep(self.sleepTime/5)        

    def simulationTankBuffer(self, tank: Tank):

        name = tank.getAttribute(id='NAME')
        if self.__debug>=1:
            print('# TANK [simulationTankBuffer] - NAME:',name)
        
        if name in ['TQ1', 'TQ2']:

            sts = tank.getStatus()[0]
            capacity = tank.getAttribute(id='CAPACITY')
            temp = tank.getAttribute(id='TEMPERATURE')
            tempLow = tank.getAttribute(id='TEMP.LOW')
            tempHigh = tank.getAttribute(id='TEMP.HIGH')
            level = capacity*(tank.getAttribute(id='LEVEL')/100)
            levelLow = capacity*(tank.getAttribute(id='LEVEL.LOW')/100)
            levelHigh= capacity*(tank.getAttribute(id='LEVEL.HIGH')/100)

            if self.__debug>=2:
                print(f'>> TANK [{name}] - Dados:','\n',
                    'STATUS',':',tank.getStatus(),'\n',
                    'CAPACITY',':',capacity,'\n',
                    'TEMPERATURE',':',temp,'C°\n',
                    'TEMP.LOW',':',tempLow,'C°\n',
                    'TEMP.HIGH',':',tempHigh,'C°\n',
                    'LEVEL',':',tank.getAttribute(id='LEVEL'),f'- VOLUME: {level}','\n',
                    'LEVEL.LOW',':',tank.getAttribute(id='LEVEL.LOW'),f'({levelLow})','\n',
                    'LEVEL.HIGH',':',tank.getAttribute(id='LEVEL.HIGH'),f'({levelHigh})','\n',
                    )

            if sts == 0: # IS WAITING
                if level >= (levelLow*2):
                    tank.setStatus(id=1) # TO AVAILABLE
                    self.__ciclosTqAvaliables = 0
                else:
                    tank.setStatus(id=2) # TO FILLING
                    self.__ciclosTqFill = 0

            if sts == 1: # IS AVAILABLE
                self.__ciclosTqAvaliables += 1
                if ((level <= (levelLow*2)) and (level > levelLow)):
                    tank.setStatus(id=2) # TO FILLING
                    self.__ciclosTqAvaliables = 0
                    self.__ciclosTqFill = 0
                elif ((level > (levelLow*2)) and 
                      (self.__ciclosTqAvaliables>self.__ciclosTqAvaliablesMax)):
                    tank.setStatus(id=2) # TO FILLING
                    self.__ciclosTqAvaliables = 0
                    self.__ciclosTqFill = 0
                else:
                    if self.__debug>=1:
                        print('AVAILABLE',
                              f'looping [{self.__ciclosTqAvaliables}/{self.__ciclosTqAvaliablesMax}]')

            if sts == 2: # TO FILLING
                self.__ciclosTqFill += 1
                if level >= levelHigh:
                    tank.setStatus(id=0) # TO WAITING
                    self.__ciclosTqFill = 0
                elif ((level >= (levelLow*3)) and
                      (self.__ciclosTqFill>=self.__ciclosTqFillMax) and
                      (temp >= tempHigh)):
                    tank.setStatus(id=3) # TO COOLING
                    self.__ciclosTqFill = 0
                    self.__ciclosTqColl = 0
                elif ((level >= (levelLow*3)) and
                      (self.__ciclosTqFill>=self.__ciclosTqFillMax) and
                      (temp < tempHigh)):
                    tank.setStatus(id=0) # TO WAITING
                    self.__ciclosTqFill = 0
                else:
                    addLiters = capacity*(random.randint(7,12)/1000) # 0.7% - 1.2%
                    addTemp = random.randint(600,900)/10
                    newLevel = int(((level + addLiters)/capacity)*100)
                    newTemp  = round(((addLiters*addTemp)+(level*temp))/(addLiters+level),2)
                    tank.setAttribute(id='LEVEL' , value=newLevel)
                    tank.setAttribute(id='VOLUME' , value=round((level + addLiters), 2))
                    tank.setAttribute(id='TEMPERATURE' , value=newTemp)
                    if self.__debug>=1:
                        print('FILLING',
                            f'looping [{self.__ciclosTqFill}/{self.__ciclosTqFillMax}]:', 
                            'addLiters=',addLiters,';',
                            'newLevel=',newLevel,';',
                            'level=',level,';',
                            'capacity=',capacity,';',
                            'temp=',temp,';',
                            'newTemp=',newTemp, '\n'
                            )
                    
            if sts == 3: # TO COOLING
                self.__ciclosTqColl += 1
                degrees = round((tempHigh-tempLow)/self.__ciclosTqCollMax,2)
                if temp < tempLow:
                    tank.setStatus(id=2) # TO FILLING
                    self.__ciclosTqColl = 0
                    self.__ciclosTqFill = 0
                elif (((temp >= tempLow) and
                       (temp <= tempHigh)) and
                      (self.__ciclosTqColl>=self.__ciclosTqCollMax)):
                    tank.setStatus(id=0) # TO WAITING
                    self.__ciclosTqColl = 0
                    self.__ciclosTqFill = 0
                else:
                    tank.setAttribute(id='TEMPERATURE' , value=round(temp-degrees,2))
                    if self.__debug>=1:
                        print('COOLING',
                            f'[{self.__ciclosTqColl}/{self.__ciclosTqCollMax}]:',
                            'temp=',temp,';',
                            'degrees=',degrees,';',
                            'tempLow=',tempLow,';',
                            'tempHigh=',tempHigh, '\n'
                            )
                    
            self.simulationColler(tank)
            self.simulationValves(tank)

            # ALARMS
            if (temp<tempLow) or (temp>tempHigh):
                tank.setAttribute(id='TEMP.ALARM' , value=1)
            else:
                tank.setAttribute(id='TEMP.ALARM' , value=0)

            if (level<levelLow):
                tank.setAttribute(id='LEVEL.LOW.ALARM' , value=1)
                tank.setAttribute(id='LEVEL.HIGH.ALARM' , value=0)
            elif(level>levelHigh):
                tank.setAttribute(id='LEVEL.LOW.ALARM' , value=0)
                tank.setAttribute(id='LEVEL.HIGH.ALARM' , value=1)
            else:
                tank.setAttribute(id='LEVEL.LOW.ALARM' , value=0)
                tank.setAttribute(id='LEVEL.HIGH.ALARM' , value=0)


    def simulationColler(self, tank: Tank):
        name = tank.getAttribute(id='NAME')
        sts = tank.getStatus()[0]
        cooler = None

        if name=='TQ1':
            cooler = self.__cooler_1
        elif name=='TQ2':
            cooler = self.__cooler_2
        else:
            cooler = None

        # if self.__debug>=2:
        #     print('# COOLER [simulationColler] - Tank:',name, '- Cooler:', cooler.getAttribute(id='NAME'))

        if sts==3: # COOLING
            newVal = tank.getAttribute(id='TEMPERATURE')
            newVal = round(newVal-(newVal*0.20),2)
            cooler.setAttribute(id='TEMPERATURE', value=newVal)
            cooler.setStatus(id=1)
        else:
            cooler.setAttribute(id='TEMPERATURE', value=tank.getAttribute(id='TEMPERATURE'))
            cooler.setStatus(id=0)

    def simulationValves(self, tank: Tank):
        name = tank.getAttribute(id='NAME')
        sts = tank.getStatus()[0]

        valve_IN = None
        valve_RET= None
        valve_OUT= None
        pump = None

        if name=='TQ1':
            valve_IN = self.__valve_1_IN
            valve_RET= self.__valve_1_RET
            valve_OUT= self.__valve_1_OUT
            pump = self.__pump_1
        elif name=='TQ2':
            valve_IN = self.__valve_2_IN
            valve_RET= self.__valve_2_RET
            valve_OUT= self.__valve_2_OUT
            pump = self.__pump_2
        else:
            valve_IN = None
            valve_RET= None
            valve_OUT= None
            pump = None

        # if self.__debug>=2:
        #     print('# VALVES [simulationValves] - Tank:',name )

        if (sts == 0) or (sts == 1): # IS AVAILABLE OR WAITING
            valve_IN.setStatus(id=0)
            valve_IN.setAttribute(id='POSITION', value=0)
            valve_RET.setStatus(id=0)
            valve_RET.setAttribute(id='POSITION', value=0)
            valve_OUT.setStatus(id=0)
            valve_OUT.setAttribute(id='POSITION', value=0)
            pump.setStatus(id=0)
            pump.setAttribute(id='OPERATION', value=0)
        elif sts == 2: # IS FILLING
            valve_IN.setStatus(id=1)
            valve_IN.setAttribute(id='POSITION', value=1)
            valve_RET.setStatus(id=0)
            valve_RET.setAttribute(id='POSITION', value=0)
            valve_OUT.setStatus(id=0)
            valve_OUT.setAttribute(id='POSITION', value=0)
            pump.setStatus(id=0)
            pump.setAttribute(id='OPERATION', value=0)            
        elif sts == 3: # IS COOLING
            valve_IN.setStatus(id=0)
            valve_IN.setAttribute(id='POSITION', value=0)
            valve_RET.setStatus(id=1)
            valve_RET.setAttribute(id='POSITION', value=1)
            valve_OUT.setStatus(id=0)
            valve_OUT.setAttribute(id='POSITION', value=0)
            pump.setStatus(id=1)
            pump.setAttribute(id='OPERATION', value=1)            
        else:
            print('# VALVES [simulationValves] - Tank:',name, 'Status (unmapped):', sts )

# MQTT
def on_connect(client, userdata, flags, rc):

    if rc == 0:
        print("# MQTT - Connected to broker!")
    else:
        print("# MQTT - Connection failed - ERROR!")


# Main
if __name__ == "__main__":

    # Define parameters
    mqtt_broker = 'broker.hivemq.com'
    mqtt_port = 1883

    # MQTT broker
    client = paho.Client("MyProcessSimulation")         #create new instance
    #client.username_pw_set(user, password=password)    #set username and password
    client.on_connect= on_connect                       #attach function to callback
    client.connect(host=mqtt_broker, port=mqtt_port)    #connect to broker

    client.loop_start()

    # Simulação
    process = ProcessSimulation(mqtt_client=client, mqtt_prefix='scadalts/sm', sleepTime=5, debugLevel=1)

    client.publish(f"scadalts/sm/PROCESS/DATE", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(3)
    
    try:
        # for i in range(600):
        while True:
            process.simulationLogic()
            time.sleep(process.sleepTime/2)
    except KeyboardInterrupt:
        print("### Interrupted process! ###")
        client.disconnect()
        client.loop_stop()
    




