#!/usr/bin/env python 3

import os

IP_range = input("Enter CIDR: ")
#Example: 192.168.125.0/24
print("")
print("#" * 50)
print("\nCommencing nmap scan of possible DNS Servers listening on port 53...\n")
print("#" * 50)
print("")
nmap_scan = os.system("sudo nmap -sT " + IP_range + " -p 53 --open -oG dns_scan.txt > scan.txt")
dns_up = os.system("cat dns_scan.txt | grep 'Up' | awk '{print $2}' > dns_up.txt")

d = open("dns_up.txt", "r")
num_up = len(d.readlines())
print("Nmap scan discovered " + str(num_up) + " open DNS ports\n")
print("A reverse lookup will now be attempted...\n")

f = open("dns_up.txt", "r")

for line in f:
	print("")
	print("#" * 50)
	print("\nAttempting Reverse DNS Lookup for " + line)
	rDNS = os.system(("dnsrecon -r " + IP_range + " -n " + line))
f.close()

os.system("rm scan.txt dns_up.txt")

print("Scan Completed! You're welcome bro!")

