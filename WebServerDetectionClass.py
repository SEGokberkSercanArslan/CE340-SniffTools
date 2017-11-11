
import nmap


class WebServerDetection():
    def __init__(self):
        self.serverList = []
        self.nm = nmap.PortScanner()

    def getServerAddress(self):
        print("Please input 10 server address")
        for i in range(10):
            self.serverList.append(input("Please input {}:".format(i)))

    def webServerDetection(self):
        self.getServerAddress()
        file = open("web.dat","a")
        for i in range(len(self.serverList)):
            self.nm.scan("{}".format(self.serverList[i]),"0-1024")
            print(self.nm.csv())
            file.writelines(self.nm.csv())

wsd = WebServerDetection()
wsd.webServerDetection()
