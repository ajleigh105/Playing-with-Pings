#iporting
import os, random
#variables
print "Enter First portion of IP (Leave off last three digits)"
inputhostname = raw_input()
x = 0
IPList = []

#main loop
while x <= 255:
    x = x + 1
    hostname = str(inputhostname) + str(x)
    response = os.system("ping -n 1 " + hostname)
    if response == 0:
           IPList.append(hostname)

#put addresses in order
print "sort list? (y/n):"
yes_or_no = raw_input() 
if yes_or_no == "y" or "Y":
    IPList.sort()

#print out IP List
for ip in IPList:
    print "Device online at " + ip
raw_input()
