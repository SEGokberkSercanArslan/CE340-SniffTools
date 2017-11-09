

import Functions

print("Welcome to Scapy Tool")

# brief documentation of each 7 functions
print("Available functions are as follows; type in function name to use it:"
      "[icmp] : Ping an IP range and collect IP addresses of the hosts that are alive and save the result. "
      "[port-id] : Find and identify ports on valid live hosts and save the results. Uses the file from function [icmp]. Run icmp first before running this function."
      "[open-port-id] : Scan valid live hosts, find open ports from each host and save the results. Again, uses the file created by [icmp]. "
      "[OS-id] : Identify operating systems (OS) and OS versions of the hosts with open ports. This function uses the file created by [open-port-id]. "
      "[firewall] : Scan and find neighbor router and firewall addresses, protocols, and ports of each router. Save the result. "
      "[snmp-detec] : Scan and find neighbor hosts addresses having the SNMP-protocols, and ports of each host. Save the result. "
      "[syn-flood] : Launch SYN-flood attack to a given destination (IP) and port(s). "
      "[show] : Display the results files created so far.")

while True:

    choice = input("Your choice :")

    if choice=="icmp":
        ICMP_ECHO_Prototype()

    elif choice == "port-id":
        #func
    elif choice == "open-port-id":
        #func
    elif choice == "OS-id":
        OS_fingerprint()

    elif choice == "firewall":
        firewall_detection()

    elif choice == "snmp-detec":

    elif choice == "syn-flood":

    elif choice == "show":
        show()

    elif choice =="exit":
        break
    else
        print("Invalid request."
              "Please type in a function or 'exit' to stop the program.")

