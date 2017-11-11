
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
        self.isOpen()

    def isOpen(self):


        "Read Ports an Source IP"
        getports = []
        openports = []


        with open("ports.dat","r") as portsdatafile:
            for line in portsdatafile.readlines():
                getports.append(line.split("\n", ))
        for i in range(len(getports)):
            openports.append(getports[i][0])


        for i in range(len(openports)):
            file = open("open_ports.dat", "a")
            if len(openports[i])>5:
                print("IP:{}".format(openports[i]))
                self.target = openports[i]
                file.write("{}\n".format(self.target))
            else :
                isOpenSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                result = isOpenSocket.connect_ex((self.target,int(openports[i])))
                if result == 0:
                    file.write("{}\n".format(openports[i]))
                    print("IP:{} and Port:{} is open".format(self.target,openports[i]))
                else:
                    print("IP:{} and Port:{} is close".format(self.target,openports[i]))
            file.close()

sc = PortScanner()
#sc.setTargetAndRun("46.253.112.23")
sc.isOpen()
