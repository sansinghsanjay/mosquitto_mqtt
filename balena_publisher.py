# libraries
import paho.mqtt.client as mqtt
import random
import time

# create mqtt client object
client = mqtt.Client()

# connect this publisher to the mosquitto broker
client.connect("test.mosquitto.org", 1883, 60)

# publish 30 random values after 2 second interval
for i in range(30):
	# get a random value within 0 and 100
	random_pressure_value = random.randint(0, 100)
	# publish this value
	client.publish("topic/string/sansingh", random_pressure_value)
	# update status
	print(i, ". Sent: ", random_pressure_value)
	# pause execution for 2 seconds
	time.sleep(2)

# disconnect client
client.disconnect()
