import sys
import pexpect
import time

DEVICE = sys.argv[1]
child = pexpect.spawn("bluetoothctl")

# Remove prior connections
print("Removing old Connections")
child.sendline("remove {}".format(DEVICE))
time.sleep(2)

# Connect to the device.
print("Pairing to"),
print(DEVICE)
child.sendline("agent on")
child.expect("Agent registered", timeout=5)
child.sendline("default-agent")
child.expect("Default agent request successful", timeout=5)
child.sendline("scan on")
time.sleep(1)
child.sendline("scan off")
child.sendline("pair {}".format(DEVICE))
time.sleep(1)
child.expect("Pairing successful", timeout=20)
child.sendline("trust {}".format(DEVICE))
print("Paried "),
print(DEVICE)
