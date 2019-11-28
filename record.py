import time
from const import *


class Log:
    def __init__(self):
        self.start_ts = None
        self.start_tf = None
        self.end_ts = None
        self.end_tf = None
        self.log_ts = None
        self.cnt = 0
        self.fcnt = 0
        
    def timer_start(self):
        self.start_ts = time.time()
        self.start_tf = time.strftime("%m-%d %H:%M:%S", time.localtime())
        self.log_ts = time.strftime("%y%m%d-%H%M%S", time.localtime())
    
    def timer_end(self):
        self.end_ts = time.time()
        self.end_tf = time.strftime("%m-%d %H:%M:%S", time.localtime())

    def cfg_output(self, device):
        if device is None:
            return 0
        
        with open(CFG_FILE, "w") as fo:
            fo.write(device)

    def cfg_input(self):
        try:
            with open(CFG_FILE, "r") as fo:
                prev_port = fo.readline()
                return prev_port
        except FileNotFoundError:
            return ''
        
    def log_output(self, device):
        log_name = "spt"+self.log_ts+".log"
        with open(log_name, "w") as fo:
            fo.write(" Serial port name:")
            fo.write('\n ')
            fo.write(device)
            fo.write('\n')
            fo.write("---------------------------------\n")
            fo.write(" Succeed count : %d \n" % (self.cnt-self.fcnt))
            fo.write(" Failed count  : %d \n" % self.fcnt)
            fo.write(" Success rate  : %.2f%% \n" % ((self.cnt-self.fcnt)/self.cnt*100))
            fo.write(" Start time    : %s\n" % self.start_tf)
            fo.write(" End time      : %s\n" % self.end_tf)
            fo.write(" Execution time: %.2fs \n" % (self.end_ts-self.start_ts))
            fo.write("\n")
        with open(log_name, "r") as fo:
            print(fo.read())
