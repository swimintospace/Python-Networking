#!/usr/bin/env python3
#Functionality: Changes the MAC address of supplied interface with randomly generated MAC Address.
# 1) Supply interface to change MAC address.
# 2) Generates a new MAC Address.
# 3) Change to generated MAC Address.

import random,subprocess

print("Script changes MAC address of current machine to randomly generated MAC addresses.")

#Supply interface for MAC address to be changed.
interface = input("Supply interface to change MAC addresses for: ")
#Generate random MAC address for NIC Card.
random_mac = "02:00:00:%02x:%02x:%02x" % (random.randint(1,255), random.randint(0,255), random.randint(0,255))
#Print random MAC address and interface to screen.
print("Generated Random MAC: " + random_mac)
print("Changing" + interface + " to " + random_mac)
#Change MAC address using subprocess library.
##Set supplied interface to DOWN.
subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "down"])
##Changed supplied interface to generated MAC.
subprocess.run(["sudo", "ip", "set", "dev", interface, "address", random_mac])
##Set supplied interface to UP.
subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "up"])
#Print final result.
print("Interface" + interface + "changed to"  + random_mac)