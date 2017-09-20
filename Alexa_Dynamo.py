### -----------   Python Code  ------------###
import csv
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import pandas as pd

### ------------- Start Alexa Stuff  ---------###

app = Flask(__name__)
ask = Ask(app, "/")
#logging.getLogger("flask_ask").setLevel(logging.DEBUG)

###  -----------  Switch Function --------------###

def setSwitch(Switchboard, switch, new_state): 
    switch_df = pd.read_csv(Switchboard + ".csv") 
    switch_df = switch_df.set_index('switch') 
    switch_df.set_value(switch,'state',new_state)
    switch_df.to_csv(Switchboard + ".csv")
	
###  -----------  Switch Function --------------###

def ReadInfo(Switchboard): 
	info_df = pd.read_csv(Switchboard + ".csv") 
	count = info_df.loc[0, 'Count']
	return count

	
###  -----------  Launch Skill --------------###
	
@ask.launch
def start_skill():
    welcome_message = 'Hello, what would you like to ask the architect'
    return question(welcome_message)

###  -------------- Say Hello --------------- ####

@ask.intent("hello")
def hello():
    setSwitch('C:\\sfdug\\Alexa','switch00', '1')
    msg = "Hello San Francisco Dynamo user group"
    return statement(msg)

###  -------------- Create Points --------------- ####
@ask.intent("CreatePoints")
def CreatePoints():
    setSwitch('C:\\sfdug\\Alexa','switch01', '1')
    msg = "I am creating the points for the Janet Echelman sculptor"
    return statement(msg)
	
###  -------------- Create Connection --------------- ####
@ask.intent("CreateConnection")
def CreateConnection():
    setSwitch('C:\\sfdug\\Alexa','switch02', '1')
    msg = "I am creating a connection between the points"
    return statement(msg)

###  -------------- Create Framing --------------- ####
@ask.intent("CreateFraming")
def CreateFraming():
    setSwitch('C:\\sfdug\\Alexa','switch03', '1')
    msg = "I am creating the framing for the Janet Echelman sculptor"
    return statement(msg)
	
###  -------------- Reset --------------- ####
@ask.intent("Reset")
def Reset():
	setSwitch('C:\\sfdug\\Alexa','switch01', '0')
	setSwitch('C:\\sfdug\\Alexa','switch02', '0')
	setSwitch('C:\\sfdug\\Alexa','switch03', '0')
	msg = "I have reset Revvit" 
	return statement(msg)

	
###  -------------- Count Framing --------------- ####
@ask.intent("CountFraming")
def CountFraming():
    info = ReadInfo('C:\\sfdug\\AlexaRead')
    msg = "I have counted: {}".format(info)
    return statement(msg)

### --------------- Port for Ngrok  -------------##

if __name__ == '__main__':   
    port = 9000 #the custom port you want
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)