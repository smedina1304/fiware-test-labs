#
# Classe: ProcessSimulation
#

# [START import_module]
import time
import random
import getopt, sys
import paho.mqtt.client as paho

from typing import List

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
        self.__tank_1.setAttribute(id='TEMPERATURE' , value=23.7)

        self.__tank_2 = Tank()
        self.__tank_2.setAttribute(id='NAME' , value='TQ2')
        self.__tank_2.setAttribute(id='LEVEL.HIGH' , value=90)
        self.__tank_2.setAttribute(id='LEVEL.LOW' , value=10)
        self.__tank_2.setAttribute(id='TEMP.HIGH' , value=30)
        self.__tank_2.setAttribute(id='TEMP.LOW' , value=20)        
        self.__tank_2.setAttribute(id='CAPACITY' , value=40000)
        self.__tank_2.setAttribute(id='CAPACITY.UNIT' , value='LT')
        self.__tank_2.setAttribute(id='TEMPERATURE' , value=24.2) 
      
        self.__tank_3 = Tank()
        self.__tank_3.setAttribute(id='NAME' , value='TQ3')
        self.__tank_3.setAttribute(id='LEVEL.HIGH' , value=90)
        self.__tank_3.setAttribute(id='LEVEL.LOW' , value=10)
        self.__tank_3.setAttribute(id='TEMP.HIGH' , value=40)
        self.__tank_3.setAttribute(id='TEMP.LOW' , value=20)        
        self.__tank_3.setAttribute(id='CAPACITY' , value=60000)
        self.__tank_3.setAttribute(id='CAPACITY.UNIT' , value='LT')
        self.__tank_3.setAttribute(id='TEMPERATURE' , value=21.7) 

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
        self.__ciclosTqCollMax = 15 

        self.__ciclosBlAvaliables = 0
        self.__ciclosBlAvaliablesMax = 30

        self.__litrosCiclo = 400
        self.__litrosLote = 0
        self.__litrosLoteMax = 25600

        self.__totalLotes = 0

        ## Simulação
        self.__tank_1.setAttribute(id='LEVEL' , value=52)
        self.__tank_1.setAttribute(id='VOLUME' , value=18300)
        self.__tank_1.setAttribute(id='TEMPERATURE' , value=41.7)

        self.__tank_2.setAttribute(id='LEVEL' , value=90)
        self.__tank_2.setAttribute(id='VOLUME' , value=36000)
        self.__tank_2.setAttribute(id='TEMPERATURE' , value=28.2)

        ## MQTT
        self.mqtt_client.publish(f"{self.mqtt_prefix}/PROCESS/DATE", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  


    def simulationLogic(self):

        # TANKS BUFFERS
        for tk in [self.__tank_1, self.__tank_2]:
            self.simulationTankBuffer(tk)

        # TANK BLENDER
        self.simulationTankBlender(tankBuffes=[self.__tank_1, self.__tank_2], tankBlender=self.__tank_3)

        self.mqtt_client.publish(f"{self.mqtt_prefix}/PROCESS/TOTAL.LOTE", self.__totalLotes)

        # TANKS Publish
        for tk in [self.__tank_1, self.__tank_2,self.__tank_3]:
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

        for valve_OUT in [self.__valve_1_OUT, self.__valve_2_OUT, self.__valve_3_OUT]:
            sentData = valve_OUT.publishMQTT(self.mqtt_client, self.mqtt_prefix)
            if self.__debug>=2:
                print('## MQTT', valve_OUT.getAttribute(id='NAME'), ":\n", sentData)

        time.sleep(self.sleepTime/5)

        # PUMPS
        for pump in [self.__pump_1, self.__pump_2, self.__pump_3]:
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
                    # TQ1 = 1,0% - 2,0%; TQ2 = 1,5% - 2,2%
                    rd = random.randint(10,20) if name=='TQ1' else random.randint(15,24)
                    addLiters = capacity*(rd/1000) 
                    addTemp = random.randint(400,700)/10
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


    def simulationTankBlender(self, tankBuffes: List[Tank], tankBlender: Tank):

        name = tankBlender.getAttribute(id='NAME')
        if self.__debug>=1:
            print('# TANK [simulationTankBlender] - NAME:',name)
        
        if name in ['TQ3']:

            sts = tankBlender.getStatus()[0]
            capacity = tankBlender.getAttribute(id='CAPACITY')
            temp = tankBlender.getAttribute(id='TEMPERATURE')
            tempLow = tankBlender.getAttribute(id='TEMP.LOW')
            tempHigh = tankBlender.getAttribute(id='TEMP.HIGH')
            volume = tankBlender.getAttribute(id='VOLUME')
            level = capacity*(tankBlender.getAttribute(id='LEVEL')/100)
            levelLow = capacity*(tankBlender.getAttribute(id='LEVEL.LOW')/100)
            levelHigh= capacity*(tankBlender.getAttribute(id='LEVEL.HIGH')/100)

            if self.__debug>=2:
                print(f'>> TANK [{name}] - Dados:','\n',
                    'STATUS',':',tankBlender.getStatus(),'\n',
                    'CAPACITY',':',capacity,'\n',
                    'TEMPERATURE',':',temp,'C°\n',
                    'TEMP.LOW',':',tempLow,'C°\n',
                    'TEMP.HIGH',':',tempHigh,'C°\n',
                    'LEVEL',':',tankBlender.getAttribute(id='LEVEL'),f'- VOLUME: {level}','\n',
                    'LEVEL.LOW',':',tankBlender.getAttribute(id='LEVEL.LOW'),f'({levelLow})','\n',
                    'LEVEL.HIGH',':',tankBlender.getAttribute(id='LEVEL.HIGH'),f'({levelHigh})','\n',
                    )
                

            if sts == 0: # IS WAITING
                if (level >= (levelLow*2)):
                    tankBlender.setStatus(id=1) # TO AVAILABLE
                else:
                    allAvailables = True
                    for tb in tankBuffes:
                        stsTB = tb.getStatus()[0]

                        if (allAvailables) and (stsTB!=1):
                            allAvailables=False

                    if allAvailables:
                        tankBlender.setStatus(id=2) # TO FILLING

                        for tb in tankBuffes:
                            tb.setStatus(id=4) # TO TRANSFER

            if sts == 1: # TO AVAILABLE
                self.__ciclosBlAvaliables += 1

                if ((level > self.__litrosLoteMax) and
                    (self.__ciclosBlAvaliables>(self.__ciclosBlAvaliablesMax/2))):
                    tankBlender.setStatus(id=4) # TO TRANSFER

                elif ((level <= levelHigh) and
                    (self.__ciclosBlAvaliables>self.__ciclosBlAvaliablesMax)):
                    allAvailables = True
                    for tb in tankBuffes:
                        stsTB = tb.getStatus()[0]

                        if (allAvailables) and (stsTB!=1):
                            allAvailables=False

                    if allAvailables:
                        tankBlender.setStatus(id=2) # TO FILLING

                        for tb in tankBuffes:
                            tb.setStatus(id=4) # TO TRANSFER
                    self.__ciclosBlAvaliables = 0
                else:
                    if self.__debug>=1:
                        print('AVAILABLE BLENDER',
                              f'looping [{self.__ciclosBlAvaliables}/{self.__ciclosBlAvaliablesMax}]')

            if sts == 2: # TO FILLING
                valve_OUT= self.__valve_3_OUT
                pump = self.__pump_3

                valve_OUT.setStatus(id=0)
                valve_OUT.setAttribute(id='POSITION', value=0)
                pump.setStatus(id=0)
                pump.setAttribute(id='OPERATION', value=0)
                
                tq1 = tankBuffes[0]
                tq2 = tankBuffes[1]

                levelLowTQ1 = tq1.getAttribute(id='LEVEL.LOW.ALARM')
                levelLowTQ2 = tq2.getAttribute(id='LEVEL.LOW.ALARM')
                
                if (levelLowTQ1==1) or (levelLowTQ2==1) or (level >= levelHigh):
                    tankBlender.setStatus(id=1) # TO AVAILABLE
                    for tb in tankBuffes:
                        tb.setStatus(id=0) # TO WAIT
                else:
                    capacityTQ1 = tq1.getAttribute(id='CAPACITY')
                    capacityTQ2 = tq2.getAttribute(id='CAPACITY')

                    volumeTQ1 = tq1.getAttribute(id='VOLUME')
                    volumeTQ2 = tq2.getAttribute(id='VOLUME')

                    tempTQ1 = tq1.getAttribute(id='TEMPERATURE')
                    tempTQ2 = tq2.getAttribute(id='TEMPERATURE')

                    addLiters = round(capacity*(random.randint(3,7)/1000),0) # 0.3% - 0.7%
                    
                    if self.__debug>=1:
                        print(
                            'BLENDER FILLING (BEFORE)',
                            'Volume TQ1=',volumeTQ1,';',
                            'Volume TQ2=',volumeTQ2,';',
                            'Liters=',addLiters,';',
                            'Liters TQ1=',(addLiters*(-1)),';',
                            'Liters TQ2=',(addLiters*2*(-1)), '\n'
                            )

                    volumeTQ1 = volumeTQ1-addLiters
                    tq1.setAttribute(id='LEVEL' , value=int((volumeTQ1/capacityTQ1)*100))

                    volumeTQ2 = volumeTQ2-(addLiters*2)
                    tq2.setAttribute(id='LEVEL' , value=int((volumeTQ2/capacityTQ2)*100))

                    tankBlender.setAttribute(id='LEVEL' , value=int(((volume+(addLiters*3))/capacity)*100))

                    tq1.setAttribute(id='VOLUME' , value=round(volumeTQ1, 2))
                    tq2.setAttribute(id='VOLUME' , value=round(volumeTQ2, 2))
                    tankBlender.setAttribute(id='VOLUME' , value=round((volume+(addLiters*3)), 2))

                    newTemp = round(((addLiters*tempTQ1)+((addLiters*2)*tempTQ2)+(temp*volume))/((addLiters*3)+volume),2)
                    tankBlender.setAttribute(id='TEMPERATURE' , value=newTemp)

                    if self.__debug>=1:
                        print('BLENDER FILLING (AFTER)',
                            'Volume TQ1=',volumeTQ1,';',
                            'Volume TQ2=',volumeTQ2,';',
                            'level TQ3=',int(((level+(addLiters*3))/capacity)*100),';',
                            'volume TQ3=',round((level+(addLiters*3)), 2), '\n'
                            )

            if sts == 4: # TO TRANSFER
                valve_OUT= self.__valve_3_OUT
                pump = self.__pump_3

                valve_OUT.setStatus(id=1)
                valve_OUT.setAttribute(id='POSITION', value=1)
                pump.setStatus(id=1)
                pump.setAttribute(id='OPERATION', value=1)

                if (level < levelLow):
                    tankBlender.setStatus(id=0) # TO WAIT
                else:
                    self.__litrosLote += self.__litrosCiclo

                    tankBlender.setAttribute(id='VOLUME' , value=round((volume - self.__litrosCiclo), 2))
                    tankBlender.setAttribute(id='LEVEL' , value=int(((volume - self.__litrosCiclo)/capacity)*100))

                    if self.__litrosLote > self.__litrosLoteMax:
                        self.__totalLotes += 1
                        self.__litrosLote = self.__litrosLote-self.__litrosLoteMax

                        if self.__litrosLote < self.__litrosLoteMax:
                            tankBlender.setStatus(id=0) # TO WAIT

                    if self.__debug>=1:
                        print('BLENDER TRANSFER',
                            'Volume (AFTER) =',volume,';',
                            'Volume (BEFORE)=',(volume - self.__litrosCiclo),';',
                            'Litres Transf. =',self.__litrosCiclo,';',
                            'Total Transf.  =',self.__litrosLote, ';',
                            'Total Lotes  =',self.__totalLotes, '\n'
                            )

            # ALARMS
            if (temp<tempLow) or (temp>tempHigh):
                tankBlender.setAttribute(id='TEMP.ALARM' , value=1)
            else:
                tankBlender.setAttribute(id='TEMP.ALARM' , value=0)

            if (level<levelLow):
                tankBlender.setAttribute(id='LEVEL.LOW.ALARM' , value=1)
                tankBlender.setAttribute(id='LEVEL.HIGH.ALARM' , value=0)
            elif(level>levelHigh):
                tankBlender.setAttribute(id='LEVEL.LOW.ALARM' , value=0)
                tankBlender.setAttribute(id='LEVEL.HIGH.ALARM' , value=1)
            else:
                tankBlender.setAttribute(id='LEVEL.LOW.ALARM' , value=0)
                tankBlender.setAttribute(id='LEVEL.HIGH.ALARM' , value=0)


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
        elif sts == 4: # IS TRANSFER
            valve_IN.setStatus(id=0)
            valve_IN.setAttribute(id='POSITION', value=0)
            valve_RET.setStatus(id=0)
            valve_RET.setAttribute(id='POSITION', value=0)
            valve_OUT.setStatus(id=1)
            valve_OUT.setAttribute(id='POSITION', value=1)
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

    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]
    
    # Options
    options = "d:"
    
    # Long options
    long_options = ["Debug="]

    # Debug Level
    debugLevel = 0

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-d", "--Debug"):
                isValid = True if currentValue in ['0', '1', '2', '3'] else False
                if not isValid:
                    debugLevel = 0
                    print (f'# ERROR: Argument ({currentArgument} = {currentValue}) is not valid!')
                    print ('> Information:', '\n', 
                           '- Arguments supported (-d or --Debug) = [0, 1, 2 or 3]')
                else:
                    debugLevel = int(currentValue)
          
    except getopt.error as err:
        print(f'# ERROR: {str(err)}', '\n\n')
        debugLevel = 0

    print(f'> Debug level setted to {debugLevel}.')

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
    process = ProcessSimulation(mqtt_client=client, mqtt_prefix='scadalts/sm', sleepTime=5, debugLevel=debugLevel)

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
    




