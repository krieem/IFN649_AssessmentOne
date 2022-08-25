import paho.mqtt.client as mqtt
from time import sleep
import serial
import paho.mqtt.client as mqtt
import os

hostname="3.11.79.48"
port=1883
mqttUser="ifn649"
mqttPass="ifn649"
def init():
    blue0 = os.path.exists("/dev/rfcomm0")
    if blue0 == False:
        os.system("sudo rfcomm bind rfcomm0 {}", com0)
        print("Teensy 1 Initialized")
        print()

def on_connect(client, userdata, flags, rc): # func for making connection print("Connected to MQTT")
    print("Connected to MQTT")
    print("Connection returned result: " + str(rc) )
    client.subscribe("ifn649")

def on_message(client, userdata, msg):
    strmsg = msg.payload
    strmsg.decode('utf-8').strip('b\'\'')
    print(strmsg)
    #print(msg.topic+" "+str(msg.payload))

def led(soil):
    actor = serial.Serial("/dev/rfcomm0", 9600)
    sleep(2)
    while True:
        if actor.in_waiting == 0:
            if (soil == '0'):
                actor.write("0".encode())
                print("LED is Green")
                break
            elif (soil != '0'):
                actor.write("1".encode())
                print("LED is Orange")
                break
        else:
            print("Connection Error")
            print("Retring in 1 second")
            print()
            sleep(1)

client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message
client.username_pw_set(mqttUser, mqttPass)
client.connect(hostname , port, 60)
client.loop_forever()
sleep(1)

#led(sensors[1])
