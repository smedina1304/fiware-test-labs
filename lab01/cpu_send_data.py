from tqdm import tqdm
from time import sleep
import requests
import json
import psutil

# Define parameters
agent_host = 'ip172-18-0-82-ch5v0m2e69v000f95390-80.direct.labs.play-with-docker.com'
#agent_host = 'localhost'
agent_port = 80

device_id = 'server001'
apikey = 'PoyryLab2023'
metrics = None

def collectData():

    #url = f"http://{agent_host}:{agent_port}/registry"
    url = f"http://{agent_host}/registry"

    headers = {"Content-Type": "application/json"}

    with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
        while True:
            rambar.n=psutil.virtual_memory().percent
            cpubar.n=psutil.cpu_percent()
            rambar.refresh()
            cpubar.refresh()

            payload = json.dumps({'device_id': f'{device_id}', 'apikey': f'{apikey}', 'metrics': {'cpu':cpubar.n, 'mem':rambar.n}})

            requests.request("POST", url, headers=headers, data=payload)

            sleep(5)

if __name__ == "__main__":
    collectData()