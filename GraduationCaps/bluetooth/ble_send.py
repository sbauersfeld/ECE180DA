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

# Write characteristic
child.sendline("char-write-req 0x0026 1234")
child.expect("Characteristic value was written successfully", timeout=10)
