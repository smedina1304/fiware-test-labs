import requests
import json
import psutil
import random

from time import sleep
from datetime import datetime
from multiprocessing import Process
from paho.mqtt import client as mqtt_client

# MQTT Parameters
broker = '192.168.0.130'
port = 1883

client_id = f'python-mqtt-{random.randint(0, 100)}' # generate client ID with pub prefix randomly
topics = [("/casaipanema50/openweather/temp_c",0),
          ("/casaipanema50/openweather/humid",0),
          ("/casaipanema50/openweather/detail_txt",0),
          ("/casaipanema50/openweather/weather_txt",0),
          ("/casaipanema50/openweather/windspeed",0),
          ("/casaipanema50/openweather/winddirection",0),
          ("/casaipanema50/openweather/clouds",0)]

# MQTT variables
temp_c = ''
humid = ''
detail_txt = ''
weather_txt = ''
windspeed = ''
winddirection = ''
clouds = ''
msg_count = 0

# Agent HTTP Parameters

agent_host = 'localhost'
agent_port = 7896

ip_labs_docker = None
#ip_labs_docker = 'ip172-18-0-63-chrkj2bqes6000dl8dc0'

if ip_labs_docker is not None:
    agent_host = f'{ip_labs_docker}-{agent_port}.direct.labs.play-with-docker.com'

start_send = True

# Calc List >> AVG 
def listAVG(lst):
    return sum(lst) / len(lst)

# Send - Functions
def sendCPU():
    t = 10

    while True:
        ram = psutil.virtual_memory().percent
        cpu = psutil.cpu_percent()
        #cpu = listAVG(psutil.cpu_percent(interval=1, percpu=True))

        if start_send:
            sendData(key='PoyryLab2023', id='server001', metrics={'cpu':cpu, 'mem':ram})

        print(f'# sendCPU (start_send:{start_send}) - [', datetime.now().strftime("%Y-%m-%d %H:%M:%S")  ,'] - metrics: {', f"'cpu':{cpu}, 'mem':{ram}", '}')
        sleep(t)

def sendData(key,id,metrics):
    url = None
    if ip_labs_docker is not None:
        url = f"http://{agent_host}/iot/json?k={key}&i={id}"
    else:
        url = f"http://{agent_host}:{agent_port}/iot/json?k={key}&i={id}"


    payload = json.dumps(metrics)
    headers = {"Content-Type": "application/json"}

    res = requests.request("POST", url, headers=headers, data=payload)
    res = None

    return res    

# MQTT - Functions
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
        global temp_c, humid, detail_txt, weather_txt, windspeed, winddirection, clouds, start_send, msg_count

        val = msg.payload.decode()
        topic = msg.topic
        print(f'# MQTT Received [', datetime.now().strftime("%Y-%m-%d %H:%M:%S")  ,']',
              '(start_send:{start_send})','\n',
              f'>> Topic:`{topic}` = `{val}`')
        
        msg_count += 1
        
        if topic.endswith('temp_c'):
            temp_c = val
        elif topic.endswith('humid'):
            humid = val
        elif topic.endswith('detail_txt'):
            detail_txt = val
        elif topic.endswith('weather_txt'):
            weather_txt = val
        elif topic.endswith('windspeed'):
            windspeed = val
        elif topic.endswith('winddirection'):
            winddirection = val
        elif topic.endswith('clouds'):
            clouds = val

        print('### Count:', msg_count)

        if start_send:
            if msg_count>=7:
                msg_count = 0
                metrics = {'temp' : temp_c, 
                    'windspeed' : windspeed, 
                    'winddirection' : winddirection,
                    'humidity' : humid,
                    'clouds': clouds,
                    'description' : detail_txt}
            
                sendData(key='PoyryWeather2023', id='station001', metrics=metrics)

                print(f'# sendWeather (sent) - [', datetime.now().strftime("%Y-%m-%d %H:%M:%S")  ,'] - metrics: ',metrics)

    client.subscribe(topics)
    client.on_message = on_message

def run_mqtt():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


# Main
if __name__ == "__main__":

    # Multiprocessing
    proc1 = Process(target=sendCPU)  # instantiating without any argument
    proc1.start()

    # Default - run_mqtt
    run_mqtt()