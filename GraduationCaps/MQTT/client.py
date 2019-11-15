# Python script to set the time on the Hexiwear
import sys
import pexpect
import time
import paho.mqtt.client as mqtt
from time import gmtime, strftime

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    print()

def main():
    DEVICE = sys.argv[1]

    client = mqtt.Client(DEVICE)
    client.connect("broker.hivemq.com")
    topic = "ee180d/group4/" + DEVICE
    client.subscribe(topic)

    client.on_message=on_message
    client.loop_start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("exiting")
        client.disconnect()
        client.loop_stop()

if __name__ == '__main__':
    main()
