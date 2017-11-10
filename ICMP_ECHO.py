
from scapy.all import *
from scapy.layers.inet import IP,ICMP

class ICMP_ECHO():
    def __init__(self):
        pass

    def icmp_prototype(self):
        first_input = input("Please input 1 for searching web address or specific ip address and 2 for local network :")
        icmpfile = open("icmp.dat", 'a')

        if int(first_input) == 1:
            try:
                destino = input("Please input destination address :")
                ans = sr1(IP(dst=destino) / ICMP() / "Hi", timeout=1)
                print("Web server is alive if you didn't see any errors")
                icmpfile.write("\n")
                icmpfile.writelines(ans[IP].src)
                print("Web IP : {}".format(ans[IP].src))
                # return ans[IP].src
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
            for i in range(int(low), int(high)):
                try:
                    ans = sr1(IP(dst="192.168.1." + str(i), ttl=64) / ICMP() / "Hi", timeout=1)
                    icmpfile.write("\n")
                    icmpfile.writelines(ans[IP].src)
                    # address_data.append(ans[IP].src)
                    print("Online : 192.168.1." + str(i))
                except TypeError:
                    print("Not Online : 192.168.1." + str(i))
            return address_data


ıcmp = ICMP_ECHO()
ıcmp.icmp_prototype()