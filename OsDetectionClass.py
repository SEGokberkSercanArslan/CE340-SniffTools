
from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP
import nmap

class OsDetection:

    def __init__(self):
        self.target = None


    def OsDetection(self):

        nm = nmap.PortScanner()
        getports = []
        openports = []

        with open("open_ports.dat", "r") as portsdatafile:
            for line in portsdatafile.readlines():
                getports.append(line.split("\n", ))
        for i in range(len(getports)):
            openports.append(getports[i][0])

        for i in range(len(openports)):
            try:
                openports[i]=int(openports[i])
            except ValueError:
                pass
        iplist=[]
        for i in range(len(openports)):
            try:
                if len(openports[i])>5:
                    iplist.append(openports[i])
            except TypeError:
                pass
        for i in range(len(iplist)):
            nm.scan("{}".format(iplist[i]),"0-1024")
            print(nm.csv())

os = OsDetection()
os.OsDetection()