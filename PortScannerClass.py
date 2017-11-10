
import socket
import threading
from queue import Queue


print_lock = threading.Lock()


class PortScanner():
    def __init__(self):
        self.target = None
        self.scannerQueue = Queue()
        self.file = open("ports.dat","a")
        self.file.write("{}\n".format(self.target))

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
                self.file.writelines("{}".format(port))

        except:
            pass

    def run(self):

        for x in range(500):
            t = threading.Thread(target=self.threadWorker)
            t.daemon = True
            t.start()

        for worker in range(1, 500):
            self.scannerQueue.put(worker)

        self.scannerQueue.join()

    def setTargetAndRun(self,ip):
        self.target=ip
        self.file.writelines("{}\n".format(self.target))
        self.run()

    def isOpen(self):
        isOpenSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = isOpenSocket.connect_ex((self.target,80))
        if result == 0:
            print("Port is open")
        else:
            print("Port Closed")

sc = PortScanner()
sc.setTargetAndRun("46.253.112.23")
sc.isOpen()
