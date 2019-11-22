import sys
import pexpect
import time

DEVICE = sys.argv[1]
child = pexpect.spawn("gatttool -I")

# Connect to the device.
print("Removing old Connections")
child.sendline("remove {0}".format(DEVICE))
time.sleep(2)

print("Pairing to"),
print(DEVICE)
child.sendline("connect {0}".format(DEVICE))
child.expect(["Connection successful","Function not implemented"], timeout=5)
print("Connected!")

command = "char-read-hnd 65"
while True:
    child.sendline(command)
    time.sleep(5)
