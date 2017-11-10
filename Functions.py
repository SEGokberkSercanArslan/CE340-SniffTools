import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP
import sys
import queue
import threading



def ICMP_ECHO_Prototype():
    first_input  = input("Please input 1 for searching web address or specific ip address and 2 for local network :")
    icmpfile = open("icmp.dat",'a')

    if int(first_input) == 1 :
        try:
            destino = input("Please input destination address :")
            ans = sr1(IP(dst=destino) / ICMP() / "Hi", timeout=1)
            print("Web server is alive if you didn't see any errors")
            icmpfile.write("\n")
            icmpfile.writelines(ans[IP].src)
            #return ans[IP].src
        except OSError:
            print("Wrong Web address or Web address not found")
            return
        except TypeError:
            print("Wrong Web address or Web address not found")
            return

    elif int(first_input) == 2:
        low = input("Please input lower scan position between 0-256:")
        high = input("Please input higher scan position between low-256:")
        address_data = []
        for i in range(int(low),int(high)):
            try:
                ans = sr1(IP(dst="192.168.1."+str(i), ttl=64) / ICMP() / "Hi", timeout=1)
                icmpfile.write("\n")
                icmpfile.writelines(ans[IP].src)
                #address_data.append(ans[IP].src)
                print("Online : 192.168.1." + str(i))
            except TypeError:
                print("Not Online : 192.168.1."+str(i))
        return address_data


def PORT_SCAN_Prototype():
    icmpfile = open("icmp.dat","r")
    onlinehosts = []
    getip = []

    "Collect ip addresses from file"
    with open("icmp.dat") as icmpdatafile:
        for line in icmpdatafile.readlines():
            getip.append(line.split("\n",))
    for i in range(len(getip)):
        onlinehosts.append(getip[i][0])



"""
def thread_port_scan_function(ip):
    ports = range(1024)
    for port in ports:
        src_port = RandShort()
        packet = IP(dst=ip)/TCP(sport=src_port, dport=port, flags='S')
        response = sr1(packet,timeout=1)
        if response:
            if response[TCP].flags == 18:
                print("Port open")
"""

thread_port_scan_function("212.101.122.35")
#PORT_SCAN_Prototype()