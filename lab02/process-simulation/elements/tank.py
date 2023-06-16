#
# Classe: Tank
#

# [START import_module]
import paho.mqtt.client as paho

from .baseElement import BaseElement
# [END import_module]



# [START - Class]
class Tank(BaseElement):
    """
    ### Classe: Tank

    Abstração do elemento Tanque do processo industrial.
    
    Volume Calc: 
    https://www.calculatorsoup.com/calculators/construction/tank.php
    
    by Sérgio C. Medina
    """

    # [METHOD - Constrution]
    def __init__(self):
       super().__init__(
           dictAttributes={
               'NAME' : '',
               'LEVEL' : 0,
               'LEVEL.HIGH' : 0,
               'LEVEL.LOW' : 0,
               'VOLUME' : 0,
               'CAPACITY' : 0,
               'CAPACITY.UNIT' : None,
               'TEMPERATURE' : 0,
               'TEMP.HIGH' : 0,
               'TEMP.LOW' : 0
           }, 
           dictStatus={
                0 : 'WAITING',
                1 : 'AVAILABLE',
                2 : 'FILLING',
                3 : 'COOLING',
                4 : 'TRANSFER',
                5 : 'CLEANING',
                6 : 'BLOCKED'
           }
       )

    def publishMQTT(self, mqtt_client:paho.Client=None, mqtt_prefix=None):
        sentData = {}
        if ((mqtt_client is not None) and
            (mqtt_prefix is not None)):
            name = self.getAttribute(id='NAME')
            attrs = list(self.getAttributes().keys())[1:]

            for attr in attrs:
                topic = f"{mqtt_prefix}/{name}/{attr}"
                value = str(self.getAttribute(id=attr))
                mqtt_client.publish(topic, value)
                sentData[topic] = value

        return sentData

# [END - Class]