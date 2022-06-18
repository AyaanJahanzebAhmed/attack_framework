import subprocess as sp

def portscan(ip):
    output = sp.getoutput('python3 port_scan.py -i'+ip)
    return output
def discovery(ip):
    output = sp.getoutput('python3 discovery.py -i'+ip)
    return output
def direnum(ip):
    output = sp.getoutput(' python3 direnum.py' + ip)
    return output
def os_disc(ip):
    output = sp.getoutput('python3 os_disc.py -i'+ip)
    return output
def google_dork(ip):
    output =sp.getoutput('python3 google_dork.py ' +ip )

