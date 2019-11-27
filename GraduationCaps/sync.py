import ntplib as ntp
from datetime import datetime
import time
import threading

ntp_pool = 'pool.ntp.org'

call = ntp.NTPClient()
response = call.request(ntp_pool, version=3)
synced_time = datetime.fromtimestamp(datetime.now().timestamp() + response.offset)
print("My device's time:\t\t", datetime.now().time())
print("Synced time:\t\t\t", synced_time.time())

print(datetime.now().timestamp())

def printTime(offset):
    synced_time = datetime.fromtimestamp(datetime.now().timestamp() + offset)
    print("Synced time 3 seconds later:\t", synced_time.time())
    print("Time offset:\t\t\t {:.4f}".format(offset))


# run_at = datetime.fromtimestamp(synced_time + 10)
# delay = (run_at - (datetime.now().timestamp() + response.offset)).total_seconds()

# threading.Timer(3, printTime, args=[response.offset]).start()