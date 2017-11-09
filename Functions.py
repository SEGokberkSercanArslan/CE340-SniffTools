import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP


def ICMP_ECHO_Prototype():
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


