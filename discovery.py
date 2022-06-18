import nmap
import optparse
nm=nmap.PortScanner()
parser = optparse.OptionParser()
parser.add_option("-i", "--ip", dest="IP",help="")
(options, arguments,) = parser.parse_args()

host = options.IP

nm.scan(host,'22-23')

print('Host : %s ' % (host))
print('State : %s' % nm[host].state())