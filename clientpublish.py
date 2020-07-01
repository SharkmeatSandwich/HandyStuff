#This script publishes data to an MQTT broker from the RaspberryPi SenseHat. 
#It also subscribes itself to a topic that enables a message to be displayed via MQTT from a Node-Red Dashboard
import paho.mqtt.client as mqtt
import time
from gpiozero import CPUTemperature
from sense_hat import SenseHat
sense = SenseHat()
# set up mqtt client
client = mqtt.Client("python_pub")
#set mqtt username/pw
client.username_pw_set(username="pi", password="PASS")
#set server to publish to
client.connect("192.168.1.58", 1883)
#Topic/s to subscribe to
client.subscribe("sense/instructions")
#define display
def display_sensehat(message):
    sense.show_message(message)
    time.sleep(10)
#define behaviour on receipt of message
def on_message(client, userdata, msg):
    message = str(msg.payload)
    print(msg.topic+" "+message)
    display_sensehat(message)
client.on_message = on_message
client.loop_start()
try:
 while True:
#publish temp to topic
  client.publish("sense/temp", round(sense.get_temperature(),2))
  client.publish("sense/tempP", round(sense.get_temperature_from_pressure(),2))
  client.publish("sense/tempH", round(sense.get_temperature_from_humidity(),2))
#publish humidity
  client.publish("sense/humid", round(sense.get_humidity(),2))
#publish pressure
  client.publish("sense/pressure", round(sense.get_pressure(),2))
#publish compass bearing to north
  client.publish("sense/compass", round(sense.get_compass(),2))
#publish x,y,z acceleration
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']
  client.publish("sense/accelx", round(x,1))
  client.publish("sense/accely", round(y,1))
  client.publish("sense/accelz", round(z,1))
#publish CPU temp
  cpu = CPUTemperature()
  client.publish("sense/CPUtemp", round(cpu.temperature,2))
#pause for 10 seconds
  time.sleep(10)
#deal nicely with ^C
except KeyboardInterrupt:
 print("interrupted!")
client.loop_stop()
