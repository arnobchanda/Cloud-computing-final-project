import json
from time import sleep
import requests
import random
import matplotlib as plt
import numpy as np
from grapher import *


URL = "http://ec2-3-144-35-49.us-east-2.compute.amazonaws.com:8080/"
value_list = [0,0,0]
response_list = ["","",""]

def post_sensor_value(sensor_number, value):
    sensor_url = URL + "sensor{}".format(sensor_number)
    value_list[i-1] = value
    r = requests.post(url=sensor_url, data=json.dumps(value))
    response_list[i-1] = r.text


d = Updater()
d.on_launch()
xdata = []
y1data = []
y2data = []
y3data = []

time = 1
while True:
    
    for i in range(1,4):
        if response_list[i-1] == "Go high":
            new_value = random.randint(value_list[i-1], 100)
        elif response_list[i-1] == "Go low":
            new_value = random.randint(0, value_list[i-1])
        elif response_list[i-1] == "Perfect":
            new_value = value_list[i-1]
        else:
            new_value = random.randint(0,100)
            
        post_sensor_value(i, new_value)    

        if i == 1:
            y1data.append(new_value)
        if i == 2:
            y2data.append(new_value)
        if i == 3:
            y3data.append(new_value)
    
    xdata.append(time)
    time+=1
    d.on_running(xdata, y1data, y2data, y3data)
    
    
    sleep(1)
    print(value_list)    
    print(response_list)
