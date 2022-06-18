import nmap
import optparse
nm=nmap.PortScanner()
parser = optparse.OptionParser()
parser.add_option("-i", "--ip", dest="IP",help="")
(options, arguments,) = parser.parse_args()

host = options.IP

nm.scan(host,'123')

for proto in nm[host].all_protocols():
    lport = nm[host][proto].keys()
    for port in lport:
        if port =='123':
            print ('port : %s\tstate : %s\tProduct :%s\tVersion :%s '%(port, nm[host][proto][port]['name'],nm[host][proto][port]['product'],nm[host][proto][port]['version']))
        else:
            print("Server not found ")


