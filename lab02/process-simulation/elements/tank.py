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
    
    by Sérgio C. Medina
    """

    # [METHOD - Constrution]
    def __init__(self):
       super().__init__(
           dictAttributes={
                'LEVEL' : 0,
                'LEVEL.HIGH' : 0,
                'LEVEL.LOW' : 0,
                'LITERS' : 0,
                'TEMPERATURE' : 0
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
       print() 


# [END - Class]