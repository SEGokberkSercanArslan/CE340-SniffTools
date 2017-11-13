
import subprocess as sub


class SniffNetwork():
    def __init__(self):
        self.source = ""
        self.target = ""
        self.portRange = ""
        self.srcPort= ""
        self.dstPort= ""

        self.sourceScript = None
        self.targetScript = None
        self.portRangeScript = None
        self.srcPortScript = None
        self.dstPortScript = None



    def getInputs(self):
        print("Please input given parameters if you don't use please input none")
        print("Necessary to input")
        self.source = str(input("Please input source IP :"))
        self.target = input("Please input target IP :")
        print("If you want range port filter please input none for next source and destination port input.")
        self.srcPort= input("Please input source port:")
        self.dstPort= input("Please input destination port:")
        print("Necessary if you didn't input others")
        self.portRange = input("Please input port range like 0-81 with (-): ")

    def setScripts(self):

        if self.source is "none" or "None":
            self.sourceScript = "192.168.1.1"
        else:
            self.sourceScript = "src host {} and".format(self.source)

        if self.target is "none" or "None":

            self.targetScript = ""
        else:
            self.targetScript = "dst host {} and".format(self.target)

        if self.srcPort is "none" or "None":
            self.srcPortScript = ""
        else:
            self.srcPortScript = "src port {} and".format(self.srcPort)

        if self.dstPort is "none" or "None":
            self.dstPortScript = ""
        else:
            self.dstPortScript = "dst port {} and".format(self.dstPort)

        if self.portRange is "none" or "None":
            self.portRangeScript = ""
        else:
            self.portRangeScript = "portrange {}".format(self.portRange)

    def sniffNetwork(self):
        self.getInputs()
        self.setScripts()

        print(self.target)
        print(self.targetScript)

        try:
            p = sub.Popen(('sudo', 'tcpdump', "{} {} {} {} {}".format(self.sourceScript,self.targetScript,self.srcPortScript
            ,self.dstPortScript,self.portRangeScript), '-l'), stdout=sub.PIPE)
            for row in iter(p.stdout.readline, b''):
                print(row.rstrip())  # process here
        except KeyboardInterrupt:
            print("Process Stopped because of keyboard interrupt ")

ok = SniffNetwork()
ok.sniffNetwork()