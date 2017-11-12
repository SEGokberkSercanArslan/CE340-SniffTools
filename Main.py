
import sys
import ICMP_ECHO
import PortScannerClass
import OsDetectionClass
import WebServerDetectionClass
import ShowClass
import SYNfloodClass

print("Welcome to Scapy Tool")

# brief documentation of each 7 functions
print("""
      Available services are as follows; type in function name to use it:
      [icmp] : Ping an IP range and collect IP addresses of the hosts that are alive and save the result. 
      [ports] : Find and identify ports on valid live hosts and save the results. Uses the file from service [icmp]. 
      Run icmp first before running this service.
      [open-ports] : Scan valid live hosts, find open ports from each host and save the results. 
            Again, uses the file created by [icmp]. 
      [OSdetection] : Identify operating systems (OS) and OS versions of the hosts with open ports. 
            This service uses the file created by [open-port-id]. 
      [web] : Scan and find 10 web-server addresses, protocols, and ports of each web server. Save the result. 
      [syn-flood] : Launch SYN-flood attack to a given destination (IP) and port(s). 
      [show] : Display the results files created so far. \n
      """)

while True:

    choice = input("Your choice :")

    if choice == "icmp":
        icmp = ICMP_ECHO()
        icmp.icmp_prototype()

    elif choice == "ports":
        sc = PortScanner()
        sc.isOpen()

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
        syn = SynFlood()
        syn.flood()

    elif choice == "show":
        s = Show()
        s.showfiles()

    elif choice == "exit":
        sys.exit(True)
    else:
        print("Invalid request. \n"
              "Please type in a service or 'exit' to stop the program. \n ")
