#
# Classe: ProcessSimulation
#

# [START import_module]
import time
import random

import paho.mqtt.client as paho

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
    def __init__(self,mqtt_client=None, mqtt_prefix=None):

        # MQTT
        self.mqtt_client = mqtt_client
        self.mqtt_prefix = mqtt_prefix
        
        # Tanks
        self.tank_1 = Tank()
        self.tank_1.setAttribute(id='NAME' , value='TQ1')
        self.tank_1.setAttribute(id='LEVEL.HIGH' , value=90)
        self.tank_1.setAttribute(id='LEVEL.LOW' , value=10)
        self.tank_1.setAttribute(id='TEMP.HIGH' , value=42)
        self.tank_1.setAttribute(id='TEMP.LOW' , value=35)        
        self.tank_1.setAttribute(id='CAPACITY' , value=35000)
        self.tank_1.setAttribute(id='CAPACITY.UNIT' , value='LT')

        self.tank_2 = Tank()
        self.tank_2.setAttribute(id='NAME' , value='TQ2')
        self.tank_2.setAttribute(id='LEVEL.HIGH' , value=90)
        self.tank_2.setAttribute(id='LEVEL.LOW' , value=10)
        self.tank_2.setAttribute(id='TEMP.HIGH' , value=30)
        self.tank_2.setAttribute(id='TEMP.LOW' , value=20)        
        self.tank_2.setAttribute(id='CAPACITY' , value=40000)
        self.tank_2.setAttribute(id='CAPACITY.UNIT' , value='LT')
        
        self.tank_3 = Tank()
        self.tank_3.setAttribute(id='NAME' , value='TQ3')
        self.tank_3.setAttribute(id='LEVEL.HIGH' , value=90)
        self.tank_3.setAttribute(id='LEVEL.LOW' , value=10)
        self.tank_2.setAttribute(id='TEMP.HIGH' , value=40)
        self.tank_2.setAttribute(id='TEMP.LOW' , value=20)        
        self.tank_3.setAttribute(id='CAPACITY' , value=60000)
        self.tank_3.setAttribute(id='CAPACITY.UNIT' , value='LT')


        # Valve
        self.valve_1_IN = Valve()
        self.valve_1_RET= Valve()
        self.valve_1_OUT= Valve()

        self.valve_2_IN = Valve()
        self.valve_2_RET= Valve()
        self.valve_2_OUT= Valve()

        self.valve_3_OUT= Valve()

        # Pump
        self.pump_1 = Pump()
        self.pump_2 = Pump()
        self.pump_3 = Pump()

        # Cooler
        self.cooler_1 = Cooler()
        self.cooler_1 = Cooler()

        # Ciclos de process
        self.ciclosTqAvaliables = 0
        self.ciclosTqAvaliablesMax = 100
        self.ciclosTqFill = 0
        self.ciclosTqFillMax = 30
        self.ciclosTqColl = 0
        self.ciclosTqCollMax = 20        

    def simulationLogic(self):

        # TANK 1
        self.simulationTankBuffer(self.tank_1)
        sentData = self.tank_1.publishMQTT(self.mqtt_client, self.mqtt_prefix)
        print('## MQTT', self.tank_1.getAttribute(id='NAME'), ":\n", sentData)

    def simulationTankBuffer(self, tank: Tank):

        name = tank.getAttribute(id='NAME')
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
                    self.ciclosTqAvaliables = 0
                else:
                    tank.setStatus(id=2) # TO FILLING
                    self.ciclosTqFill = 0

            if sts == 1: # IS AVAILABLE
                self.ciclosTqAvaliables += 1
                if ((level <= (levelLow*2)) and (level > levelLow)):
                    tank.setStatus(id=2) # TO FILLING
                    self.ciclosTqAvaliables = 0
                    self.ciclosTqFill = 0
                elif ((level > (levelLow*2)) and 
                      (self.ciclosTqAvaliables>self.ciclosTqAvaliablesMax)):
                    tank.setStatus(id=2) # TO FILLING
                    self.ciclosTqAvaliables = 0
                    self.ciclosTqFill = 0

            if sts == 2: # TO FILLING
                self.ciclosTqFill += 1
                if level >= levelHigh:
                    tank.setStatus(id=0) # TO WAITING
                    self.ciclosTqFill = 0
                elif ((level >= (levelLow*3)) and
                      (self.ciclosTqFill>=self.ciclosTqFillMax) and
                      (temp >= tempHigh)):
                    tank.setStatus(id=3) # TO COOLING
                    self.ciclosTqFill = 0
                    self.ciclosTqColl = 0
                elif ((level >= (levelLow*3)) and
                      (self.ciclosTqFill>=self.ciclosTqFillMax) and
                      (temp < tempHigh)):
                    tank.setStatus(id=0) # TO WAITING
                    self.ciclosTqFill = 0
                else:
                    addLiters = capacity*(random.randint(7,12)/1000) # 0.7% - 1.2%
                    addTemp = random.randint(600,900)/10
                    newLevel = int(((level + addLiters)/capacity)*100)
                    newTemp  = round(((addLiters*addTemp)+(level*temp))/(addLiters+level),2)
                    tank.setAttribute(id='LEVEL' , value=newLevel)
                    tank.setAttribute(id='VOLUME' , value=round((level + addLiters), 2))
                    tank.setAttribute(id='TEMPERATURE' , value=newTemp)
                    print('FILLING:', 
                        'addLiters=',addLiters,' ; ',
                        'newLevel=',newLevel,' ; ',
                        'level=',level,' ; ',
                        'capacity=',capacity,' ; ',
                        'temp=',temp,' ; ',
                        'newTemp=',newTemp, '\n'
                        )
                    
            if sts == 3: # TO COOLING
                self.ciclosTqColl += 1
                degrees = round((tempHigh-tempLow)/self.ciclosTqCollMax,2)
                if temp < tempLow:
                    tank.setStatus(id=2) # TO FILLING
                    self.ciclosTqColl = 0
                    self.ciclosTqFill = 0
                elif (((temp >= tempLow) and
                       (temp <= tempHigh)) and
                      (self.ciclosTqColl>=self.ciclosTqCollMax)):
                    tank.setStatus(id=0) # TO WAITING
                    self.ciclosTqColl = 0
                    self.ciclosTqFill = 0
                else:
                    tank.setAttribute(id='TEMPERATURE' , value=round(temp-degrees,2))
                    print('COOLING:', 
                        'temp=',temp,' ; ',
                        'degrees=',degrees,' ; ',
                        'tempLow=',tempLow,' ; ',
                        'tempHigh=',tempHigh, '\n'
                        )

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
    process = ProcessSimulation(mqtt_client=client, mqtt_prefix='scadalts/sm')

    try:
        for i in range(250):
            process.simulationLogic()
            time.sleep(5)
    except KeyboardInterrupt:
        print("### Interrupted process! ###")
        client.disconnect()
        client.loop_stop()
    




