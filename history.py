import time

def timer():
    ts = time.time()
    tf = time.strftime("%m-%d %H:%M:%S", time.localtime())
    return ts, tf

def conf_save(dev):
    if dev is None:
        return 0
        
    fo = open("serial-port-test-log", "w+")
    fo.write("Serial port name:")
    fo.write('\n')
    fo.write(dev)
    fo.write('\n')
    fo.close

def conf_read():
    try:
        fo = open("serial-port-test-log", "r")
    except FileNotFoundError:
        return ''
    fo.readline()
    str = fo.readline().splitlines()
    fo.close
    return str
    
def file_rep(cnt, fcnt, start_tf, end_tf, exe_time):
    fo = open("serial-port-test-log", "a")
    fo.write("---------------------------------\n")
    fo.write(" Succeed count : %d \n" % (cnt-fcnt))
    fo.write(" Failed count  : %d \n" % fcnt)
    fo.write(" Success rate  : %.2f%% \n" % ((cnt-fcnt)/cnt*100))
    fo.write(" Start time    : %s\n" % (start_tf))
    fo.write(" End time      : %s\n" % (end_tf))
    fo.write(" Execution time: %.2fs \n" % (exe_time))
    fo.write("\n")
    fo.close

