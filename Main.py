
import sys
from ICMP_ECHO import *
from PortScannerClass import *
from OsDetectionClass import *
from WebServerDetectionClass import *
from ShowClass import *
from SniffNetworkPrototype import *
from SynFlood import *

print("Welcome to Scapy Tool")
print("The tool was created by Gökberk Sercan Arslan and Selin Candemir")

# brief documentation of each 7 functions
print("""
      Available services are as follows; type in function name to use it:
      [icmp] : Ping an IP range and collect IP addresses of the hosts that are alive and save the result. 
      [ports] : Find and identify ports on valid live hosts and save the results. Uses the file from service [icmp]. 
      Run icmp first before running this service.
      [open-ports] : Scan valid live hosts, find open ports from each host and save the results. 
            Again, uses the file created by [icmp]. 
      [OSdetection] : Identify operating systems (OS) and OS versions of the hosts with open ports. 
            This service uses the file created by [open-ports]. 
      [web] : Scan and find 10 web-server addresses, protocols, and ports of each web server. Save the result. 
      [syn-flood] : Launch SYN-flood attack to a given destination (IP) and port(s).
       [sniff] : The tool provides to listen network given filter configuration.
      [show] : Display the results files created so far. \n
      """)

while True:

    choice = input("Your choice :")

    if choice == "icmp":
        icmp = ICMP_ECHO()
        icmp.icmp_prototype()

    elif choice == "ports":
        sc = PortScanner()
        sc.run()

    elif choice == "open-ports":
        sc = PortScanner()
        sc.isOpen()

    elif choice == "OSdetection":
        os = OsDetection()
        os.OsDetection()

    elif choice == "web":
        wsd = WebServerDetection()
        wsd.webServerDetection()

    elif choice == "syn-flood":
        syn = SynFlooadAttacker()
        syn.attack()

    elif choice == "show":
        s = Show()
        s.showfiles()

    elif choice == "sniff":
        snf = SniffNetworkPrototype()
        snf.sniff()

    elif choice == "exit":
        sys.exit(True)
    else:
        print("Invalid request. \n"
              "Please type in a service or 'exit' to stop the program. \n ")
