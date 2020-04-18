import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("test.mosquitto.org", 1883, 60)
choice = ''
while(choice != 'q'):
	message = str(raw_input("Enter message to publish: "))
	client.publish("sanjay/rocky/singh", message)
	choice = str(raw_input("Enter 'q' to quit: "))
	print("")
client.disconnect()
