

import subprocess as sub


class SniffNetworkPrototype():
    def __init__(self):
        pass

    def sniff(self):
        print("Sniff tool uses tcpdump notation standards")
        print("Ex input: src host 192.168.1.1 and portrange 0-81")
        target = input("Your input:")
        try:
            p = sub.Popen(('sudo', 'tcpdump', "{}".format(target), '-l'), stdout=sub.PIPE)
            for row in iter(p.stdout.readline, b''):
                print(row.rstrip())  # process here
        except KeyboardInterrupt:
            print("Process Stopped Because Keyboard Interrupt")

#ok = SniffNetworkPrototype()
#ok.sniff()