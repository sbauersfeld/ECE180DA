# Python script to set the time on the Hexiwear
import sys
import pexpect
import time
import paho.mqtt.client as mqtt
from time import gmtime, strftime

def main():
    devices = {"device1": "hi scott", "device2": "hi wilson", "device3": "hi jesse"}

    client = mqtt.Client("jonmyong_publish")
    client.connect("broker.hivemq.com")
    topic_base = "ee180d/group4/"
    topics = {}

    for key in devices:
        topics[key] = topic_base + key

    while True:
        for key in devices:
            client.publish(topics[key], devices[key])
        time.sleep(3)

if __name__ == '__main__':
    main()
