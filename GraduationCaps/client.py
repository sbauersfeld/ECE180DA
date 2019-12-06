import sys
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from datetime import datetime
import ntplib as ntp
import threading
import time

MSG = None
def on_message(client, userdata, msg):
    global MSG
    MSG = msg.payload.decode()

def printTime(offset, client):
    global MSG
    print("Time offset:\t {:.4f}".format(offset))
    client.loop_start()
    synced_end_time = None
    starttime = time.time()
    while True:
        if MSG != None:
            msg = MSG.split()
            if msg[0] == "Stop":
                synced_end_time = float(msg[1])
            print("Got message:", msg)
            MSG = None

        timestamp = datetime.now().timestamp() + offset
        synced_time = datetime.fromtimestamp(timestamp)

        if synced_end_time != None and timestamp >= synced_end_time:
            print("Stopping at:", synced_time.time())
            client.loop_stop()
            break
        else:
            print("Synced time:\t", synced_time.time())
            time.sleep(1.0 - ((time.time() - starttime) % 1.0))

def main():
    global MSG
    DEVICE = sys.argv[1]
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("broker.hivemq.com")
    client.subscribe("ee180d/group4/" + DEVICE)
    client.loop_start()
    msg = None
    while True:
        if MSG != None:
            msg = MSG.split()
            MSG = None
            client.loop_stop()
            break
    print(msg)
    # msg = subscribe.simple("ee180d/group4/" + DEVICE, hostname="broker.hivemq.com")
    # msg = msg.payload.decode().split()
    synced_start_time = msg[0]
    num_rows = msg[1]
    num_cols = msg[2]
    coords = msg[3:]
    print("Start time:", synced_start_time)
    print("Num rows:", num_rows)
    print("Num cols:", num_cols)
    print("My coords:", coords)

    ntp_pool = 'pool.ntp.org'

    call = ntp.NTPClient()
    response = call.request(ntp_pool, version=3)
    synced_delay = float(synced_start_time) - (datetime.now().timestamp() + response.offset)

    threading.Timer(synced_delay, printTime, args=[response.offset, client]).start()

if __name__ == '__main__':
    main()
