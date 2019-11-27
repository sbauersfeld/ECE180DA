import paho.mqtt.client as mqtt
from read_form import GetData
from read_form import GetCoords
from datetime import datetime
import ntplib as ntp

ntp_pool = 'pool.ntp.org'

def main():
    data = GetData()
    localization_info, participation_info, num_rows, num_cols, errors = GetCoords(data)
    if len(errors):
        print("Errors:\n{}\n".format(errors))

    client = mqtt.Client("jonmyong_publish")
    client.connect("broker.hivemq.com")
    topic_base = "ee180d/group4/"

    call = ntp.NTPClient()
    response = call.request(ntp_pool, version=3)
    synced_init_time = int(datetime.now().timestamp() + response.offset + 30)
    synced_time = datetime.fromtimestamp(synced_init_time)
    print("Run Function at:\t", synced_time.time())

    for key in localization_info:
        if participation_info[key] == False:
            continue
        message = str(synced_init_time) + " " + str(num_rows) + " " + str(num_cols) + " " + " ".join(str(x) for x in localization_info[key])
        print(topic_base + str(key))
        ret = client.publish(topic_base + str(key), message)
        ret.wait_for_publish()

if __name__ == '__main__':
    main()
