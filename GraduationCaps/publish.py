# Python script to set the time on the Hexiwear
import sys
import pexpect
import time
import paho.mqtt.client as mqtt
from time import gmtime, strftime
from read_form import GetData
from read_form import GetCoords

def main():
    data = GetData()
    localization_info, participation_info, num_rows, num_cols, errors = GetCoords(data)
    if len(errors):
        print("Errors:\n{}\n".format(errors))

    client = mqtt.Client("jonmyong_publish")
    client.connect("broker.hivemq.com")
    topic_base = "ee180d/group4/"

    # while True:
    for key in localization_info:
        if participation_info[key] == False:
            continue
        message = str(num_rows) + " " + str(num_cols) + " " + " ".join(str(x) for x in localization_info[key])
        print(topic_base + str(key))
        client.publish(topic_base + str(key), message)
        # time.sleep(3)

if __name__ == '__main__':
    main()
