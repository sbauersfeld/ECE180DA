import ntplib as ntp
from datetime import datetime
import time

ntp_pool = 'pool.ntp.org'

call = ntp.NTPClient()
response = call.request(ntp_pool, version=3)
synced_time = datetime.fromtimestamp(datetime.now().timestamp() + response.offset)
print("My device's time:\t\t", datetime.now().time())
print("Synced time:\t\t\t", synced_time.time())
time.sleep(1)
synced_time = datetime.fromtimestamp(datetime.now().timestamp() + response.offset)
print("Synced time 1 second later:\t", synced_time.time())
print("Time offset:\t\t\t {:.4f}".format(response.offset))