# python 3.x
# 20.05.2022
# iiotmq.com
# pub_paho_mqtt.py
# broker : https://publicmqttbroker.iiotmq.com/
# help and doc : https://www.iiotmq.com/

import paho.mqtt.client as paho
import time

broker = "publicmqttbroker.iiotmq.com"
port = 1883


def on_publish(client, userdata, result):
    print("data published")


client = paho.Client("pub_paho_mqtt")
client.username_pw_set("publicmqttbroker", "publicmqttbroker")
client.on_publish = on_publish
client.connect(broker, port)

for i in range(100):
    ret = client.publish("testtopic", """{"temperature": 21,"humidity": 23}""")
    print(ret)
    time.sleep(10)
