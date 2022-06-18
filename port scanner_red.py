import sys
import socket
import optparse
 # FUNCTION TO GET THE INPUT FROM TH USER
parser = optparse.OptionParser()
parser.add_option("-i", "--ip", dest="IP",help="")
(options, arguments,) = parser.parse_args()



ip = options.IP

open_ports = []
import ipaddress

def validate_ip_address(address):
    try:
        ipv = ipaddress.ip_address(address)
    except ValueError:
        print("IP address {} is not valid".format(address))
        quit()
# ports = range(1, 65535)
ports = {21, 22, 23, 53, 80, 135, 443, 445}
validate_ip_address(ip)

def probe_port(ip, port, result=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result


for port in ports:
    sys.stdout.flush()
    response = probe_port(ip, port)
    if response == 0:
        open_ports.append(port)

if open_ports:
    print("Open Ports are: ")
    print(sorted(open_ports))
else:
    print("Looks like no ports are open :(")