

from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP

def print_summary(pkt):
    if IP in pkt:
        ip_src=pkt[IP].src
        ip_dst=pkt[IP].dst
    if TCP in pkt:
        tcp_sport=pkt[TCP].sport
        tcp_dport=pkt[TCP].dport

        print (" IP src " + str(ip_src) + " TCP sport " + str(tcp_sport))
        print (" IP dst " + str(ip_dst) + " TCP dport " + str(tcp_dport))

#pkt = IP(dst="192.168.1.101")/ICMP()/"hi"
#print_summary(pkt)


#sniff(filter="ip",prn=print_summary)
# or it possible to filter with filter parameter...!
#sniff(filter="ip and host 192.168.0.1",prn=print_summary)

from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP
from scapy.layers import *
import sys


def ICMP_Prototype_2():
    first_input  = input("Please input 1 for searching web address or specific ip address and 2 for local network :")
    if int(first_input) == 1 :
        try:
            destino = input("Please input destination address :")
            ans = sr1(IP(dst=destino) / ICMP() / "Hi", timeout=1)
            print("Web server is alive if you didn't see any errors")
            return ans[IP].src

        except OSError:
            print("Wrong Web address or Web address not found")
            sys.exit(True)
        except TypeError:
            print("Wrong Web address or Web address not found")
            sys.exit(True)


    elif int(first_input) == 2:
        low = input("Please input lower scan position between 0-256:")
        high = input("Please input higher scan position between low-256:")
        address_data = []
        for i in range(int(low),int(high)):
            try:
                ans = sr1(IP(dst="192.168.1."+str(i), ttl=64) / ICMP() / "Hi", timeout=1)
                address_data.append(ans[IP].src)
                print("Online : 192.168.1." + str(i))
            except TypeError:
                print("Not Online : 192.168.1."+str(i))
        return address_data


#test
data = []
data = (ICMP_Prototype_2())
print(data)
