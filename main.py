from flask import Flask ,render_template,url_for,request,send_file
from flask_sqlalchemy import SQLAlchemy
import os
import command_exec
import port_scan
import netbios
import pickle,ftpp
#import dnss
import cve
import sql_brute
import xss

app=Flask(__name__)

def checkKey(dict, key):
   if key in dict.keys():
      #print("value =", dict[key])
      return True
   else:
      #print("Not present")
      return False
def reporting(ip,data,key):
    file_exists = os.path.exists('%s.txt' % ip)
    if file_exists:
        if os.path.getsize("%s.txt" % ip) == 0:
            print('File is empty')
            mydict = {key:data}
            with open('%s.txt' % ip, 'r+b') as fh:
                pickle.dump(mydict, fh)
        else:
            print("file present")
            pickle_off = open("%s.txt" % ip, "r+b")
            emp = pickle.load(pickle_off)
            v = checkKey(emp, key)
            if v:
                print("updating")
                emp[key] = data
            else:
                emp[key] = data
            pickle_off.close()
            with open('%s.txt' % ip, 'wb') as fh:
                pickle.dump(emp, fh)

    else:
        mydict = {key:data}
        with open('%s.txt' % ip, 'wb') as fh:
            pickle.dump(mydict, fh)
        print("done")

@app.route("/",methods=['POST','GET'])
@app.route("/home",methods=['POST','GET'])
@app.route("/index",methods=['POST','GET'])
def index():
    return render_template("index.html")
@app.route("/recon.html",methods=['POST','GET'])
def recon():
    return render_template("recon.html")
@app.route("/os_disc.html",methods=['POST','GET'])
def osdisc():
    return render_template("os_disc.html")
@app.route("/os_disc_res",methods=['POST','GET'])
def osdiscc():
    output = request.form
    ipp = output["ip"]
    result = command_exec.os_disc(ipp)
    reporting(str(ipp),str(result),"os_disc")
    return render_template("os_disc.html", ip=result)


@app.route("/port_scanner.html",methods=['POST','GET'])
def port_scanner():
    return render_template("port_scanner.html")
@app.route("/portscan_result",methods=['POST','GET'])
def portscan_result():
    output=request.form
    ipp =output["ip"]
    #result=command_exec.portscan(ipp)
    b = port_scan.scanner(ipp)
    reporting(str(ipp),b,"port_scan")
    return render_template("port_scanner.html",res= b)
@app.route("/scan.html",methods=['POST','GET'])
def scan():
    return render_template("scan.html")
@app.route("/enum.html",methods=['POST','GET'])
def enum():
    return render_template("enum.html")
@app.route("/discovery.html",methods=['POST','GET'])
def disc():
    return render_template("discovery.html")
@app.route("/discovery_result",methods=['POST','GET'])
def discs():
    output = request.form
    ipp = output["ip"]
    result = command_exec.discovery(ipp)
    reporting(str(ipp),result,"disc")
    #print(type(result))
    return render_template("discovery.html", ip=result)
@app.route("/ftp.html",methods=['POST','GET'])
def ftp():
    return render_template("ftp.html")
@app.route("/ftp_res.html",methods=['POST','GET'])
def ftp_res():
    output = request.form
    ipp = output["ip"]
    print(ipp)
    # result=command_exec.portscan(ipp)
    b = ftpp.enum(str(ipp))
    reporting(str(ipp),b,"ftp")
    print(b)
    return render_template("ftp.html", res=b)
@app.route("/netbios.html",methods=['POST','GET'])
def netbios():
    return render_template("netbios.html")
@app.route("/netbios_res.html",methods=['POST','GET'])
def netbios_res():
    output = request.form
    ipp = output["ip"]
    print(ipp)
    # result=command_exec.portscan(ipp)
    b = netbios.netb(str(ipp))
    reporting(str(ipp),b,"netb")
    print(b)
    return render_template("netbios.html", res=b)


@app.route("/dnss.html",methods=['POST','GET'])
def dnss():
    return render_template("dns.html")
@app.route("/dns_res.html",methods=['POST','GET'])
def dns_res():
    output = request.form
    ipp = output["ip"]
    print(ipp)
    # result=command_exec.portscan(ipp)
    b = dnss.dns_cap(str(ipp))
    reporting(str(ipp),b,"dns")
    print(b)
    return render_template("dns.html", res=b)

@app.route("/sql.html",methods=['POST','GET'])
def sqll():
    return render_template("sqlinj.html")
@app.route("/sql_res.html",methods=['POST','GET'])
def sql_res():
    output = request.form
    ipp = output["ip"]
    print(ipp)
    # result=command_exec.portscan(ipp)
    b = sql_brute.scan_sql_injection(str(ipp))
    #reporting(str(ipp),b,"sql")
    print(b)
    return render_template("sqlinj.html", res=b)
@app.route("/xss.html",methods=['POST','GET'])
def xsss():
    return render_template("xss.html")
@app.route("/xss.html",methods=['POST','GET'])
def xsss_res():
    output = request.form
    ipp = output["ip"]
    print(ipp)
    # result=command_exec.portscan(ipp)
    b = xss.core.main(str(ipp))
    print(b)
    return render_template("xss.html", res=b)


@app.route("/google_dork.html",methods=['POST','GET'])
def gd():
    return render_template("google_dork.html")
@app.route("/google_dork_res.html",methods=['POST','GET'])
def gdr():
    output = request.form
    ipp = output["ip"]
    result = command_exec.discovery(ipp)
    return render_template("google_dork.html",ip = result)
@app.route("/direnum.html",methods=['POST','GET'])
def direnum():
    return render_template("direnum.html")
@app.route("/direnum_result",methods=['POST','GET'])
def direnum_res():
    output = request.form
    ipp = output["ip"]
    result = command_exec.direnum(ipp)
    return render_template("direnum.html", ip=result)

@app.route("/hash",methods=['POST','GET'])
def hashh():
    return render_template("hash.html")


@app.route("/gain_acess.html",methods=['POST','GET'])
def gainac():
    return render_template("gain_acess.html")
@app.route("/cve.html",methods=["POST","GET"])
def cvee():
    return render_template("cve.html")
@app.route("/cve_res.html", methods=['POST', 'GET'])
def cvee_res():
    output = request.form
    ipp = output["product"]
    version=output["version"]
    if version:
        result = cve.VuldbLookup(ipp,version)
    else:
        result = cve.VuldbLookup(ipp)
    return render_template("cve.html", res=result)
@app.route("/Test.html",methods=['POST','GET'])
def testing():
    """ipp = '10.0.2.11'
    b=port_scan.scanner(ipp)
    with open('testinggg.txt', 'r+b') as fh:
        pickle.dump(b, fh)
    #result = command_exec.portscan(ipp)"""
    return render_template("test.html")
@app.route("/download1",methods=['POST','GET'])
def download_file():
    p="ftp_user.txt"
    return send_file(p,as_attachment=True)
@app.route("/priv_esc.html",methods=['POST','GET'])
def download_file_privesc():
    return render_template("priv_esc.html")
@app.route("/payloads.html",methods=['POST','GET'])
def payloads():
    return render_template("payloads.html")

@app.route("/privesc_download",methods=['POST','GET'])
def download_file_priv():
    p="privesc.py"
    return send_file(p,as_attachment=True)
@app.route("/bashtcp",methods=['POST','GET'])
def download_file_bashtcp():
    p="bashtcp.txt"
    return send_file(p,as_attachment=True)
@app.route("/bashudp",methods=['POST','GET'])
def download_file_bashudp():
    p="bashudp.txt"
    return send_file(p,as_attachment=True)
@app.route("/ipv4",methods=['POST','GET'])
def download_file_ipv4():
    p="ipv4.txt"
    return send_file(p,as_attachment=True)

@app.route("/ipv6",methods=['POST','GET'])
def download_file_ipv6():
    p="ipv6.txt"
    return send_file(p,as_attachment=True)
@app.route("/perl",methods=['POST','GET'])
def download_file_perl():
    p="perl.txt"
    return send_file(p,as_attachment=True)
@app.route("/php",methods=['POST','GET'])
def download_file_php():
    p="php.txt"
    return send_file(p,as_attachment=True)

@app.route("/java",methods=['POST','GET'])
def download_file_java():
    p="java.txt"
    return send_file(p,as_attachment=True)

@app.route("/awk",methods=['POST','GET'])
def download_file_awk():
    p="awk.txt"
    return send_file(p,as_attachment=True)
@app.route("/netcat",methods=['POST','GET'])
def download_file_netcat():
    p="netcat.txt"
    return send_file(p,as_attachment=True)
@app.route("/powershell",methods=['POST','GET'])
def download_file_powershell():
    p="powershell.txt"
    return send_file(p,as_attachment=True)
@app.route("/report.html",methods=['POST','GET'])
def report():

    return render_template("report.html")
@app.route("/report_res.html",methods=['POST','GET'])
def reportt():
    disc=None
    pc= None
    osd=None
    ftp=None
    netb=None
    dns=None

    output = request.form
    ipp = output["ip"]
    pickle_off = open("%s.txt" % ipp, "r+b")
    a = pickle.load(pickle_off)
    if checkKey(a,"port_scan"):
        pc=a.get("port_scan")
    if checkKey(a,"os_disc"):
        osd=a.get("os_disc")
    if checkKey(a,"disc"):
        disc=a.get("disc")
    if checkKey(a, "ftp"):
        ftp = a.get("ftp")
    if checkKey(a, "dns"):
        dns = a.get("dns")





    return render_template("report.html",pc=pc,osd=osd,disc=disc,ftp=ftp,netb=netb,dns=dns)
if __name__ == '__main__':
    app.run(debug=True)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
