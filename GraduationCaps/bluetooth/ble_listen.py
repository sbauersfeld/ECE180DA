import sys
import pexpect
import time

DEVICE = sys.argv[1]
child = pexpect.spawn("gatttool -I")

# Connect to device
print("Connecting to"),
print(DEVICE)
while True:
    child.sendline("connect {}".format(DEVICE))
    res = child.expect(["Connection successful","Function not implemented"], timeout=5)
    if res == 0:
        break
print("Connected!")

# Read characteristic
while True:
    child.sendline("char-read-hnd 0x0026")
    res = child.expect(["Characteristic value/descriptor: 01"], timeout=10)
    time.sleep(5)
