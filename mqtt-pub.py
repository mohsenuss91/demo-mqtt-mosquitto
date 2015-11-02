# -*- coding: utf-8 -*-
#
# MQTT publisher
#
import time
from datetime import datetime
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print "Connected with result code", str(rc)


def on_publish(client, userdata, mid):
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S%z"), "[-]",
    print 'publish!'

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_publish = on_publish
    client.on_connect = on_connect

    # # client.username_pw_set('YOUR_SECRET_KEY')
    client.connect("localhost", 18830, keepalive=60)
    client.loop_start()

    i = 0
    while 1:
        client.publish("test/mychannel", "Hello world %d" % i, qos=2)
        time.sleep(3)
        i += 1
