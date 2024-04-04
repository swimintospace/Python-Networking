#!/usr/bin/env python3
#Functionality: Script which scans networks via ARP request and response. Replies come with MAC and IP address if host found.
import scapy.all as scapy
import argparse


print("This program functions as a network scanner utility. ")
print("Usage: python3 network_scanner.py [-t] ip")
print("[-t] scan for specific IP address")
#Define arguments through argparse
def cmd_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help="Target IP address")
    args = parser.parse_args()

    if not args.target:
        parser.error("Please specify an IP address or a list of IP addresses")
    return args
#Create and scan network with specified IP Address supplied by the user.
def scan():
    answered = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip), timeout=2)[0]
    results = []
    for i in range(0, len(answered)):
        client = {"ip": answered[i][1].psrc, "mac": answered[i][1].hwsrc}
        results.append(client)

    return results
#Print scan results with IP and MAC Address
def results(result):
    print("IP Addresses \t Mac Addresses")
    for i in result:
            print("{}\t{}".format(i["ip"], i["mac"]))


args = cmd_arguments()