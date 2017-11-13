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
                openports = []
                getports = []

                with open("ports.dat", "r") as webdatafile:
                    for line in webdatafile.readlines():
                        getports.append(line.split("\n", ))
                for i in range(len(getports)):
                    openports.append(getports[i][0])

                for i in range(len(openports)):
                    if len(openports[i]) > 6:
                        print("IP : {}".format(openports[i]))
                    else:
                        print("Open Port: {}".format(openports[i]))

            elif filename[i] == "open-ports":
                openports=[]
                getports=[]

                with open("open_ports.dat", "r") as webdatafile:
                    for line in webdatafile.readlines():
                        getports.append(line.split("\n", ))
                for i in range(len(getports)):
                    openports.append(getports[i][0])

                for i in range(len(openports)):
                    if len(openports[i])>6:
                        print("IP : {}".format(openports[i]))
                    else :
                        print("Open Port: {}".format(openports[i]))

            elif filename[i] == "web":

                getports=[]
                openports=[]

                with open("web.dat", "r") as webdatafile:
                    for line in webdatafile.readlines():
                        getports.append(line.split("\n", ))
                for i in range(len(getports)):
                    openports.append(getports[i][0])

                for i in range(len(openports)):
                    print(openports[i]+"*\n")


#s = Show()
#s.showfiles()
