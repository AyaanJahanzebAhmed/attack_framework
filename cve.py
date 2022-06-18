import requests

#with open ("vuldb_api.txt","r") as f:
#	key= f.read()

def VuldbLookup (product, version=None):
	url = "https://vuldb.com/?api"
	if version:
		q="product:%s, version:%s"% (product, version)
	else:
		q="product:%s"%product


	query = {"apikey":"f481b85f473ad003ba004fe347fc5096","advancedsearch":q}

	results=requests.post(url,query)

	j=results.json()

	if "result" in j:
		sources=[result["source"] for result in j["result"] if"source" in result]
		v=[]
		for i in sources:
			a = i.get("cve")
			b = a.get("id")
			v.append(b)

		return v

	else:
		return []
""""
a=VuldbLookup("vsftpd")
print(a)
"""""