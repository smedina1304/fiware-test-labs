#
# Classe: Valve
#

# [START import_module]
from .baseElement import BaseElement
# [END import_module]



# [START - Class]
class Valve(BaseElement):
    """
    ### Classe: Valve

    Abstração do elemento Válvula do processo industrial.
    
    by Sérgio C. Medina
    """

    # [METHOD - Constrution]
    def __init__(self):
       super().__init__(
           dictAttributes={
                'POSITION' : 0
           }, 
           dictStatus={
                0 : 'CLOSED',
                1 : 'OPENED'
           }
       )
       print() 



# [END - Class]