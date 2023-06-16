import requests
import json
import time

from multiprocessing import Process, Value
from flask import Flask, request, make_response, json

# Define parameters
mqtt_broker = 'broker.hivemq.com'
mqtt_port = 1883

# Define shared variables
START = Value("i", 0)
RUNNING = Value("i", 0)
ERROR = Value("i", 0)

# Define Flask Application
app = Flask(__name__)

@app.route("/status")
def echo():
    data = {
        'START' : START.value,
        'RUNNING' : RUNNING.value,
        'ERROR' : ERROR.value
    }
    return make_response(json.dumps(DATA), 200)

@app.route("/start/on", methods=["GET"])
def starton():
    return start(request, va=1)

@app.route("/start/off", methods=["GET"])
def starton():
    return start(request, va=1)

def start(request, val=0):
    # Validação do Retorno
    msg = None
    cod = 0

    # GET
    if request.method == "GET":

        if START.value == 0:
            START.value = 1
            cod = 200
            msg = {'success':cod,'message':"Started",'detail':f'attribute START == {START.value} (ON=1; OFF=0)'}            
        else:
            cod = 412
            msg = {'error':cod,'message':'Precondition Failed',f'START: {START.value}':'attribute START no changed! (ON=1; OFF=0)'}

    # OTHERS
    else:
        cod = 405
        msg = {'error':cod,'message':'Method Not Allowed','detail':f'method {request.method} not supported by this URL'}        

    # RESPONSE
    return make_response(json.dumps(msg), cod)

# Multiprocessing
#p = Process(target=getOpenweathermap).start()

# Main
if __name__ == "__main__":
    getOpenweathermap()