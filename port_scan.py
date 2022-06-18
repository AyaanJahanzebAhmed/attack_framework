import nmap
import optparse
nm=nmap.PortScanner()
parser = optparse.OptionParser()
parser.add_option("-i", "--ip", dest="IP",help="")
(options, arguments,) = parser.parse_args()
def scanner(ipp):
    host = ipp
    nm.scan(host,'15-200')


    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        data={}
        for port in lport:
            data1={port:{'state':nm[host][proto][port]['name'],'product':nm[host][proto][port]['product'],'version':nm[host][proto][port]['version']}}
            data.update(data1)
        #print ('port : %s\tstate : %s\tProduct :%s\tersion :%s '%(port, nm[host][proto][port]['name'],nm[host][proto][port]['product'],nm[host][proto][port]['version']))
        return data