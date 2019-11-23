import sys
import paho.mqtt.client as mqtt_client
import paho.mqtt.subscribe as subscribe

class Client:
    def __init__(self, my_id):
        self.id = my_id
        self.num_rows = 0
        self.num_cols = 0
        self.coords = []

    def on_message(self, client, userdata, message):
        msg = str(message.payload.decode("utf-8")).split()
        print(msg)
        if len(msg) == 0:
            return
        self.num_rows = msg[0]
        self.num_cols = msg[1]
        self.coords = msg[2:]
        client.disconnect()
        client.loop_stop()

    def get_info(self):
        client = mqtt_client.Client(self.id)
        client.connect("broker.hivemq.com")
        topic = "ee180d/group4/" + self.id
        print(topic)
        client.subscribe(topic)

        client.on_message=self.on_message
        client.loop_forever()

def main():
    DEVICE = sys.argv[1]
    # my_client = Client(DEVICE)
    # my_client.get_info()
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
