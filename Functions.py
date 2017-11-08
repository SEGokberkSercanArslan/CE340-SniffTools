from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP


def ICMP_Prototype_2():
    first_input  = input("Please input 1 for searching we address and 2 for local network :")
    if int(first_input) == 1 :
        try:
            destino = input("Please input destination address :")
            ans = sr1(IP(dst=destino, ttl=64) / ICMP() / "Hi", timeout=1)
            print("Web server is  alive")
            return ans[IP].src
        except OSError:
            print("Wrong Web address or Web address not found")
        finally:
            return
    elif int(first_input) == 2:
        scan_range = input("Please input scan range between 0-256 :")
        address_data = []
        for i in range(int(scan_range)):
            try:
                ans = sr1(IP(dst="192.168.1."+str(i), ttl=64) / ICMP() / "Hi", timeout=1)
                print("Online : 192.168.1."+str(i))
                address_data.append(ans[IP].src)
            except TypeError:
                print("Not Online : 192.168.1."+str(i))
        return address_data


#test
data = []
data = (ICMP_Prototype_2())
print(data)
