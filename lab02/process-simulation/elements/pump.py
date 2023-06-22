#
# Classe: Pump
#

# [START import_module]
from .baseElement import BaseElement
# [END import_module]



# [START - Class]
class Pump(BaseElement):
    """
    ### Classe: Pump

    Abstração do elemento Bomba do processo industrial.
    
    by Sérgio C. Medina
    """

    # [METHOD - Constrution]
    def __init__(self):
       super().__init__(
           dictAttributes={
               'NAME' : '',
               'OPERATION' : 0
           }, 
           dictStatus={
               0 : 'OFF',
               1 : 'ON'
           }
       )

# [END - Class]