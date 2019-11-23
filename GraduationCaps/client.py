import sys
import paho.mqtt.client as mqtt_client
import paho.mqtt.subscribe as subscribe
from datetime import datetime
import ntplib as ntp
import threading

def main():
    DEVICE = sys.argv[1]
    msg = subscribe.simple("ee180d/group4/" + DEVICE, hostname="broker.hivemq.com")
    msg = msg.payload.decode().split()
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
    synced_time = datetime.fromtimestamp(datetime.now().timestamp() + response.offset)
    print("Got message at:\t", synced_time.time())
    synced_delay = float(synced_start_time) - (datetime.now().timestamp() + response.offset)

    def printTime(offset):
        synced_time = datetime.fromtimestamp(datetime.now().timestamp() + offset)
        print("Synced time 30 seconds later:\t", synced_time.time())
        print("Time offset:\t\t\t {:.4f}".format(offset))

    threading.Timer(synced_delay, printTime, args=[response.offset]).start()

if __name__ == '__main__':
    main()
