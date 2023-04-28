import requests
import json

from flask import Flask, request, make_response, json

# Define parameters
agent_host = 'fiware-iot-agent-json'
agent_port = 7896

# Define shared variables
DATA = {}
SEND = False

# Define Flask Application
app = Flask(__name__)

@app.route("/echo")
def echo():
    return make_response(json.dumps(DATA), 200)


@app.route("/command", methods=["GET", "POST"])
def command():
    global SEND    

    # Validação do Retorno
    msg = None
    cod = 0

    # POST
    if request.method == "POST":
        data = request.json
        if "switch" in data:
            if SEND == False:
                SEND = True
                cod = 200
                msg = {"switch": "Started sending data"}
            elif SEND == True:
                SEND = False
                cod = 200
                msg = {"switch": "Stopped sending data"}
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