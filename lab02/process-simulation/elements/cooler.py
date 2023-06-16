#
# Classe: Cooler
#

# [START import_module]
from .baseElement import BaseElement
# [END import_module]


# [START - Class]
class Cooler(BaseElement):
    """
    ### Classe: Cooler

    Abstração do elemento Válvula do processo industrial.
    
    by Sérgio C. Medina
    """

    # [METHOD - Constrution]
    def __init__(self):
       super().__init__(
           dictAttributes={
                'TEMPERATURE' : 0
           }, 
           dictStatus={
                0 : 'WAITING',
                1 : 'COOLING'
           }
       )


# [END - Class]