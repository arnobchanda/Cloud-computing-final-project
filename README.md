# Cloud-computing-final-project
This is a final project for CISC 681 Cloud computing course for Harrisburg university

## Project Idea
The main idea is to offset resource intensive tasks to the cloud.
In this project we have assume we have 3 tempreture sensors and 3 tempreture regulators. 
The client's job is to just send the data over to the cloud.
The cloud makes the decision of what to do with the data.

## Pseudo Code

Computer -> Acts like tempreture sensors(RNG), and tempreture regualtors(RNG)

Loop:

	Computer -> measures tempreture
	Computer -> Sends data to AWS cloud
	AWS Cloud -> Makes decision on setting tempreture high, low or no change.
	AWS Cloud -> Responds to computer with command
	Computer -> Sets a new tempreture based on command
	
Repeat Loop

## Python pre-requisites
1. matplotlib (Might have to install)
2. numpy  (Might have to install)
3. json (Comes with python)
4. requests (Comes with python)
5. http.server (Comes with python 3.7+)

## How to run

To run server

```
python3 server.py
```

To run client

```
python3 client.py
```
