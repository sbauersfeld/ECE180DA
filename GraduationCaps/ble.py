import sys
import pexpect
import time

DEVICE = sys.argv[1]
child = pexpect.spawn("bluetoothctl")

# Connect to the device.
print("Removing old Connections")
child.sendline("remove {0}".format(DEVICE))
time.sleep(2)
print("Pairing to"),
print(DEVICE)
child.sendline("agent on")
child.expect("Agent registered", timeout=5)
child.sendline("default-agent")
child.expect("Default agent request successful", timeout=5)
child.sendline("scan on")
time.sleep(1)
child.sendline("scan off")
child.sendline("pair {0}".format(DEVICE))
time.sleep(1)
code=raw_input("Code: ")
child.sendline("{0}".format(code))
child.expect("Pairing successful", timeout=20)
print("Paried "),
print(DEVICE)
child.sendline("disconnect {0}".format(DEVICE))
time.sleep(1)
child.sendline("quit")
