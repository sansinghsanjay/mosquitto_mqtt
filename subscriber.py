import paho.mqtt.client as mqtt

def on_connect(client, user_data, flags, return_code):
	print("Connected successfully with return code : ", return_code)
	client.subscribe("topic/string/sansingh")

def on_message(client, user_data, message):
	global message_count
	message_count = message_count + 1
	print(message_count, ". ", message.payload.decode())
	#client.disconnect()

message_count = 0

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
