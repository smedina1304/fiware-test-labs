#
# Classe: Tank
#

# [START import_module]
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
               'LEVEL.HIGH.ALARM' : 0,
               'LEVEL.LOW' : 0,
               'LEVEL.LOW.ALARM' : 0,
               'VOLUME' : 0,
               'CAPACITY' : 0,
               'CAPACITY.UNIT' : None,
               'TEMPERATURE' : 0,
               'TEMP.ALARM' : 0,
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

# [END - Class]