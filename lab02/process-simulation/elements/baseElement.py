#
# Classe: BaseElement
#

# [START import_module]
import paho.mqtt.client as paho
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

    def publishMQTT(self, mqtt_client:paho.Client=None, mqtt_prefix=None, fiware_services_key=None):
        """
        Metodo publishMQTT

        Utilizado para atualizar os atributos e status do elemento 
        em um o servidor MQTT definido

        OBS: IMPORTANTE - É necessário que existe o atributo 'NAME'
        para o elemento, pois é utilizado na composição do Tópico.

        Parametros:
        - mqtt_client: Classe de conexão com o Server MQTT
        - mqtt_prefix: Prefixo do Tópico que receberá o valor
        - fiware_services_key: Chave do serviço do FIWARE para o padrão "UltraLight" para iotAgente MQTT
        """

        prefixes = [mqtt_prefix, f'ul/{fiware_services_key}' ]
        sentData = {}
        topic = None
        value = None
        
        if ((mqtt_client is not None) and
            (mqtt_prefix is not None)):
            name = self.getAttribute(id='NAME')

            for prefix in prefixes:
                # Atributos
                attrs = list(self.getAttributes().keys())[1:]
                for attr in attrs:
                    if prefix.startswith('ul/'):
                        topic = f"{prefix}/{name}/attrs"
                        value = f"{name}|{str(self.getAttribute(id=attr))}"                      
                    else:
                        topic = f"{prefix}/{name}/{attr}"
                        value = str(self.getAttribute(id=attr))

                    mqtt_client.publish(topic, value)
                    sentData[topic] = value

                # Status
                if prefix.startswith('ul/'):
                    topic = f"{prefix}/{name}/attrs"
                    value = f"STATUS.ID|{str(self.getStatus()[0])}"
                else:
                    topic = f"{prefix}/{name}/STATUS.ID"
                    value = str(self.getStatus()[0])
                mqtt_client.publish(topic, value)
                sentData[topic] = value

                if prefix.startswith('ul/'):
                    topic = f"{prefix}/{name}/attrs"
                    value = f"STATUS.DESC|{str(self.getStatus()[1])}"
                else:
                    topic = f"{prefix}/{name}/STATUS.DESC"
                    value = str(self.getStatus()[1])
                mqtt_client.publish(topic, value)
                sentData[topic] = value

        return sentData

# [END - Class]