
import socket
import threading
from queue import Queue


print_lock = threading.Lock()


class PortScanner():
    def __init__(self):
        self.target = "46.253.112.23"
        self.scannerQueue = Queue()


    def threadWorker(self):
        while True:
            worker = self.scannerQueue.get()
            self.portScan(worker)
            self.scannerQueue.task_done()

    def portScan(self,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((self.target, port))
            with print_lock:
                print("port {} is open".format(port))
                file = open("ports.dat","a")
                file.write("{}\n".format(port))
                file.close()
        except:
            pass

    def run(self):

        for x in range(500):
            t = threading.Thread(target=self.threadWorker)
            t.daemon = True
            t.start()

        for worker in range(1,500):
            self.scannerQueue.put(worker)

        self.scannerQueue.join()

    def setTargetAndRun(self,ip):
        self.target=ip
        file = open("ports.dat","a")
        file.write("{}\n".format(self.target))
        file.close()
        self.run()

    def isOpen(self):

        isOpenFile = open("open_ports.dat", "a")
        isOpenFile.write("{}\n".format(self.target))

        "Read Ports an Source IP"
        counter = 0
        getports = []
        openports = []
        searchportset = []

        with open("ports.dat","r") as portsdatafile:
            for line in portsdatafile.readlines():
                getports.append(line.split("\n", ))
        for i in range(len(getports)):
            openports.append(getports[i][0])
        for i in range(len(openports)):
            if len(openports[i])>5:
                searchportset[counter].append(openports[i])
                counter+=1
            else:
                searchportset[counter-1].append(openports[i])
        print(searchportset)


        isOpenSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = isOpenSocket.connect_ex((self.target,80))
        if result == 0:
            print("Port is open")
        else:
            print("Port Closed")

sc = PortScanner()
#sc.setTargetAndRun("46.253.112.23")
sc.isOpen()
