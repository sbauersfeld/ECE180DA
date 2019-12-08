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

    client = mqtt.Client()
    client.connect("broker.hivemq.com")
    topic_base = "ee180d/group4/"

    call = ntp.NTPClient()
    response = call.request(ntp_pool, version=3)
    end_time = int(datetime.now().timestamp() + response.offset + 5)
    message = "Stop " + str(end_time)

    for key in localization_info:
        ret = client.publish(topic_base + str(key), message)
        ret.wait_for_publish()
        
    synced_end_time = datetime.fromtimestamp(end_time)
    print("Stop at:", synced_end_time.time())

if __name__ == "__main__":
    main()