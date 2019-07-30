def conf_save(dev):
    if dev is None:
        return 0
        
    fo = open("serial-port-test-log", "w+")
    fo.write("Serial port name:")
    fo.write('\n')
    fo.write(dev)
    
    fo.close

def conf_read():
    try:
        fo = open("serial-port-test-log", "r")
    except FileNotFoundError:
        return ''
    fo.readline()
    str = fo.readline()
    fo.close
    return str
    
def file_rep(count, failed_count, start_time, end_time, execution_time):
    fo = open("serial-port-test-log", "a")
    fo.write('\n')
    fo.write("\n")
    fo.write(" Succeed count:\t\t%15d \n" % (count-failed_count))
    fo.write(" Failed count:\t\t%15d \n" % failed_count)
    fo.write(" Success rate:\t\t%14.2f%% \n" % ((count-failed_count)/count*100))
    fo.write(" Start time: \t\t%s\n" % (start_time))
    fo.write(" End time: \t\t%s\n" % (end_time))
    fo.write(" Execution time:\t %13.2fs \n" % (execution_time))
    fo.write("\n")
    fo.close
