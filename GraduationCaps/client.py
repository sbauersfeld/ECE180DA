import sys
import paho.mqtt.client as mqtt_client
import paho.mqtt.subscribe as subscribe

def main():
    DEVICE = sys.argv[1]
    msg = subscribe.simple("ee180d/group4/" + DEVICE, hostname="broker.hivemq.com")
    msg = msg.payload.decode().split()
    num_rows = msg[0]
    num_cols = msg[1]
    coords = msg[2:]
    print("Num rows:", num_rows)
    print("Num cols:", num_cols)
    print("My coords:", coords)

if __name__ == '__main__':
    main()
