import subprocess as sp
import re
def netb(ip):
    b = sp.getoutput("nbtscan -v -s : " +ip)
    a = str(b)
    c = re.split("\n", a)
    d = []
# print(c)
    for a in c:
        e = a.split(":")

        d.append(e)

    d.pop()
    return (d)
#netb("10.0.2.11")