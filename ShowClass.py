class Show():
    def __init__(self):
        pass

    def showfiles(self):

        a = input("""
            Which file(s)? Seperate files by space,
            available files are: icmp, ports, open-ports, web \n""")

        filename = a.split()

        for i in range(0, len(filename)):

            if filename[i] == "icmp":
                file = open("icmp.dat")
                print("Alive host IP's are: \n")
                s = file.readline()
                while s != "":
                    print(s)
                    s = file.readline()
                file.close()

            elif filename[i] == "ports":
                file = open("ports.dat")
                line = file.readline()
                while line != "":
                    if "." in line:
                        print("IP: ", line, " port(s) :")
                    line = file.readline()
                    print(line)
                file.close()

            elif filename[i] == "open-ports":
                file = open("open_ports.dat")
                line = file.readline()
                while line != "":
                    if "." in line:
                        print("IP: ", line, " port(s) :")
                    line = file.readline()
                    print(line)
                file.close()


            elif filename[i] == "web":
                file = open("web.dat")
                line = file.readline()
                while line != "":
                    if line == "host;hostname;hostname_type;protocol;port;name;state;" \
                               "product;extrainfo;reason;version;conf;cpe":
                        line = file.readline()

                        while line != "host;hostname;hostname_type;protocol;port;name;state;" \
                                      "product;extrainfo;reason;version;conf;cpe":
                            print("\n")
                            current = line.split(";")
                            print("host: ", current[0], " hostname: ", current[1], "hostname type: ", current[2],
                                  "protocol: ", current[3], "port: ", current[4], "name: ", current[5], "state: ",
                                  current[6], "product: ", current[7], "extra info: ", current[8], "reason: ",
                                  current[9], "version: ", current[10], "conf: ", current[11], "cpe: ", current[12],
                                  "\n")
                            line = file.readline()
                file.close()


s = Show()
s.showfiles()
