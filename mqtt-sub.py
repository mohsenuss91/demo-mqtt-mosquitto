# -*- coding: utf-8 -*-
#
# MQTT subscriber
#
import paho.mqtt.client as mqtt
from datetime import datetime


def on_connect(client, userdata, flags, rc):
    print "Connected with result code", str(rc)
    client.subscribe("test/mychannel", qos=2)


def on_message(client, userdata, msg):

    print msg.retain
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S%z"), "[-]",
    print "qos: {qos}, topic: {topic}, payload: {payload}".format(
        qos=msg.qos,
        topic=msg.topic,
        payload=msg.payload
    )


def on_publish(client, userdata, mid):
    print userdata, mid

if __name__ == '__main__':
    client_id = "abcdef"
    client = mqtt.Client(client_id=client_id, clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message

    # client.username_pw_set('YOUR_SECRET_KEY')
    client.connect("localhost", 18830, keepalive=60)
    # client.loop_start()
    client.loop_forever()
