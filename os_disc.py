from scapy.all import *
from scapy.layers.inet import IP,ICMP
import optparse
 # FUNCTION TO GET THE INPUT FROM TH USER
parser = optparse.OptionParser()
parser.add_option("-i", "--ip", dest="IP",help="")
(options, arguments,) = parser.parse_args()

ip = options.IP
pack=IP(dst=ip)/ICMP()
resp=sr1(pack,timeout=10)

if resp== None:
	print("OS not detected")
elif IP in resp:
	if (resp.getlayer(IP).ttl) <= 64:
		os="The OS of the server is linux"
	else:
		os="The OS of the server is Windows"
print(os)