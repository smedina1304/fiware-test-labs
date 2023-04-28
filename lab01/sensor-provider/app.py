import requests
import json
import time

from multiprocessing import Process, Value
from flask import Flask, request, make_response, json

# Define parameters
agent_host = 'fiware-iot-agent-json'
agent_port = 7896

# Define shared variables
DATA = {}

STATION = Value("b", False)
INTERVAL = Value("i", 5)

# Define Flask Application
app = Flask(__name__)

@app.route("/echo")
def echo():
    return make_response(json.dumps(DATA), 200)


@app.route("/command", methods=["GET", "POST"])
def command():

    # Validação do Retorno
    msg = None
    cod = 0

    # POST
    if request.method == "POST":
        data = request.json
        if "switch" in data:
            if STATION.value == False:
                STATION.value = True
                cod = 200
                msg = {"switch": "Started sending data"}
            elif STATION.value == True:
                STATION.value = False
                cod = 200
                msg = {"switch": "Stopped sending data"}
            else:
                cod = 405
                msg = {"error": "Method not allowed"}

        elif "interval" in data:
            try:
                INTERVAL.value = int(data["interval"])
                cod = 200
                msg = {"interval": f"Interval changed: {INTERVAL.value}"}
            except:
                cod = 405
                msg = {"error": "Method not allowed"}                

        else:
            cod = 405
            msg = {"error": "Method not allowed"}


    # GET
    elif request.method == "GET":
        cod = 412
        msg = {'error':cod,'message':'Precondition Failed','detail':'attribute metrics is no data available'}

    # OTHERS
    else:
        cod = 405
        msg = {'error':cod,'message':'Method Not Allowed','detail':f'method {request.method} not supported by this URL'}        

    # RESPONSE
    return make_response(json.dumps(msg), cod)



@app.route("/registry", methods=['GET', 'POST'])
def registry():
    if request.method == "POST":
        print(f"received: {request.json}")

        # Request Mensagem
        req = request.json

        # Variaveis para extrair os dados da Request
        device_id = None
        apikey = None
        metrics = None

        for key in req:
            if key.lower()=='device_id':
                device_id = req[key]
            elif key.lower()=='apikey':
                apikey = req[key]
            elif key.lower()=='metrics':
                metrics = req[key]

        # Validação do Retorno
        msg = None
        cod = 0

        if device_id is None:
            cod = 412
            msg = {'error':cod,'message':'Precondition Failed','detail':'attribute device_id is no data available'}
        elif apikey is None:
            cod = 412
            msg = {'error':cod,'message':'Precondition Failed','detail':'attribute apikey is no data available'}            
        elif metrics is None:
            cod = 412
            msg = {'error':cod,'message':'Precondition Failed','detail':'attribute metrics is no data available'}             
        else:
            global DATA
            
            DATA[device_id] = {'device_id': f'{device_id}', 'apikey': f'{apikey}', 'metrics': metrics}

            sendData(key=apikey, id=device_id, metrics=metrics)

            cod = 202
            msg = {'success':cod,'message':'Accepted','detail':'received data'}  


    elif request.method == "GET":
        cod = 412
        msg = {'error':cod,'message':'Precondition Failed','detail':'attribute metrics is no data available'}
    else:
        cod = 405
        msg = {'error':cod,'message':'Method Not Allowed','detail':f'method {request.method} not supported by this URL'}        

    return make_response(json.dumps(msg), cod)


def sendData(key,id,metrics):
    url = f"http://{agent_host}:{agent_port}/iot/json?k={key}&i={id}"

    payload = json.dumps(metrics)
    headers = {"Content-Type": "application/json"}

    res = requests.request("POST", url, headers=headers, data=payload)

    return res

def getOpenweathermap():
    # Paramertros
    lat = -23.631927550736076
    lon = -46.71247713068783
    appid = '65007142e8f726b54bf467b1441052a8'
    metrics = {'temp' : 0, 
                'feels_like' : 0, 
                'pressure' : 0,
                'humidity' : 0,
                'description' : 'Stopped'}
    
    # URL de solicitação dos dados
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}&lang=pt_br&units=metric'

    #Looping
    while True:
        if STATION.value:
            res = requests.get(url)
            if res.status_code == 200:
                data = res.json()
                try: 
                    temp = data['main']['temp']
                    feels_like = data['main']['feels_like']
                    pressure = data['main']['pressure']
                    humidity = data['main']['humidity']
                    description = data['weather'][0]['description']
                    metrics = {'temp' : temp, 
                            'feels_like' : feels_like, 
                            'pressure' : pressure,
                            'humidity' : humidity,
                            'description' : description}
                except:
                    metrics = {'temp' : 0, 
                            'feels_like' : 0, 
                            'pressure' : 0,
                            'humidity' : 0,
                            'description' : 'Error'}
            else:
                metrics = {'temp' : 0, 
                        'feels_like' : 0, 
                        'pressure' : 0,
                        'humidity' : 0,
                        'description' : f'HTTP Error: {res.status_code}'}                    
            
            sendData(key=appid, id='station001', metrics=metrics)


        time.sleep(INTERVAL.value)

# Multiprocessing
p = Process(target=sendData).start()

# Main
if __name__ == "__main__":
    getOpenweathermap()