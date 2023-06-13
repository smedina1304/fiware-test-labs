import psutil
import os
import numpy as np
import pandas as pd

from time import sleep
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Calc List >> AVG 
def listAVG(lst):
    return round(sum(lst) / len(lst),2)

# CPU 
def cpu_predict(df):
    # Pré-processamento dos dados
    df['date_time'] = pd.to_datetime(df['date_time'])
    df['timestamp'] = df['date_time'].map(datetime.timestamp)
    df['timestamp'] = (df['timestamp'] - df['timestamp'].min()) / 5

    # Divisão dos dados em treinamento e teste
    X = df[['timestamp']]
    y = df['cpu_percent']

    # Treinamento do modelo
    poly_features = PolynomialFeatures(degree=2)
    X_poly = poly_features.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)

    # Previsão
    time_prev = []
    current_time = datetime.now()
    for p in range(0,5):
        current_time = (current_time + timedelta(seconds=10)).replace(microsecond=0)
        time_prev.append(current_time)
        

    # Preparação dos dados para previsão
    X_test = poly_features.transform([time_prev])

    # Realização da previsão
    cpu_percent_pred = model.predict(X_test)[0]
    
    # Impressão da previsão
    print(f"Previsão de consumo de CPU às {current_time}: {cpu_percent_pred}")


# Main
if __name__ == "__main__":
    t = 10

    path_file_out = './df_metrics.csv'

    df = None

    while True:
        ram = psutil.virtual_memory().percent
        cpu = psutil.cpu_percent(interval=1)
        cpulst = psutil.cpu_percent(interval=1, percpu=True)
        cpuavg = listAVG(cpulst)

        metrics = {
            'date_time'   : [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            'cpu_percent' : [cpu],
            'mem_percent' : [ram],
            'cpu_average' : [cpuavg],
            'pid_len'     : [len(psutil.pids())],
            'cpu_listval' : [','.join(str(x) for x in cpulst)]
        }

        print(metrics)

        if df is None:
            df = pd.DataFrame.from_dict(metrics)
        else:
            df = pd.concat([df, pd.DataFrame.from_dict(metrics)], axis=0, ignore_index=True)

        check_save = (df.shape[0]%50)==0
        is_save = False

        if check_save:
            df.to_csv(path_file_out, index=False)
            is_save = True
            print('DF Shape:', df.shape[0], ' - ' , 'Saved' if is_save else 'Memory' )

            # if df.shape[0]>500:
            #     cpu_predict(df[['date_time','cpu_percent']].tail(500))

        sleep(t)