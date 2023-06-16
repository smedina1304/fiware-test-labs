#
# Classe: BaseElement
#

# [START import_module]

# [END import_module]



# [START - Class]
class BaseElement:
    """
    ### Classe: BaseElement

    Classe base para herança dos elementos do processo.
    
    by Sérgio C. Medina
    """

    # [METHOD - Constrution]
    def __init__(self, dictAttributes={}, dictStatus=[]):
        """
        Metodo inicial

        Parametros:
        - dictAttributes: Definição da lista de atributos definidospor (ID, VALUE)
        - dictStatus: Definição da lista de status ou estados do elemento definidos por (ID, VALUE)
        """

        self.__attrib = dictAttributes
        self.__stlist = dictStatus
        self.__status = 0
        
    def getAttributes(self):
        """
        Metodo getAttributes

        Utilizado para retornar a lista de atributos

        Parametros:
        - None
        """
        return self.__attrib
        

    def getAttribute(self, id):
        """
        Metodo getAttribute

        Utilizado para retornar o valor do atributo

        Parametros:
        - id: 'String' de identificação do atributo
        """
        try:
            return self.__attrib[id]
        except KeyError:
            return None


    def setAttribute(self, id=None, value=None):
        """
        Metodo setAttribute

        Utilizado para atualizar o valor do atributo

        Parametros:
        - id: 'String' de identificação do atributo
        - value: Valor a ser atualizado para o atributo
        """
        try:
            if id in self.__attrib.keys():
                self.__attrib[id] = value
            else:
                print(f'Method setAttribute: Key Error {id} not exists!')
                raise(KeyError)
        except KeyError:
            return None
        

    def getStatusList(self):
        """
        Metodo getStatus

        Utilizado para retornar a lista de status

        Parametros:
        - None
        """
        return self.__stlist
        

    def getStatus(self):
        """
        Metodo getStatus

        Utilizado para retornar o valor do status

        Parametros:
        - None
        """
        try:
            return self.__status, self.__stlist[self.__status]
        except KeyError:
            return None


    def setStatus(self, id=None):
        """
        Metodo setStatus

        Utilizado para atualizar o valor do status

        Parametros:
        - id: 'String' de identificação do status
        """
        try:
            if id in self.__stlist.keys():
                self.__status = id
            else:
                print(f'Method setStatus: Key Error "{id}" not exists!')
                raise(KeyError)
        except KeyError:
            return None


# [END - Class]