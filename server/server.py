#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json
from urllib import response

# Make server availaible on port 8080
hostname = "0.0.0.0"
port = 8080

# Function to edit the readings.json file
def sensor_editor(sensor_number, value):
    with open("readings.json", "r") as f:
        data = json.load(f)
    
    sensor_name = "sensor{}".format(sensor_number)
    data[sensor_name] = value
    
    with open("readings.json", "w") as f:
        json.dump(data, f)

        
class MyServer(BaseHTTPRequestHandler):
    store_path = os.path.join(os.curdir, 'readings.json')
    def do_GET(self):
        
        # Make the reading file availaible at http://URL:8080/sensor-readings
        if self.path == '/sensor-readings':
            with open(self.store_path) as f:
                self.send_response(200)
                self.send_header("Content-type", "text/json")
                self.end_headers()
                self.wfile.write(f.read().encode())
        
        # Print this line for every other URL possibility      
        else:        
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("This is Cloud Computing Final Project by Arnob Chanda", "utf-8"))
    
    # Allow upload of sensor reading on individual URL.
    # Sensor 1 data is uploaded to http://URL:8080/sensor1
    # Sensor 2 data is uploaded to http://URL:8080/sensor2
    # and so forth. Can be scaled by just increasing the for loop.
        
    def do_POST(self):
        for i in range(1,4):       
            sensor_path="/sensor{}".format(i)     
            if self.path == sensor_path:
                length = self.headers['content-length']
                value = self.rfile.read(int(length))
                sensor_val = int(value.decode())
                
                sensor_editor(i,sensor_val)
                
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                
                # Tempreture regulator control logic
                if(sensor_val < 50):
                    response_text="Go high"
                elif (sensor_val > 50):
                    response_text="Go low"
                elif (sensor_val == 50):
                    response_text="Perfect"
                
                self.wfile.write(bytes(response_text, "utf-8"))
                 
        
if __name__ == "__main__":
    webserver = HTTPServer((hostname, port), MyServer)
    print("Server Started")
    
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass
    
    webserver.server_close()
    print("Server Stopped")