import requests
import argparse
import sys

#parser = argparse.ArgumentParser()

#parser.add_argument('-w','--wordlist', type=str, required=True,help="Switch for Wordlist")
#parser.add_argument('-u','--url', type=str, required=True, help="Switch for URL")
#args = parser.parse_args()
def direnumm(url):
	ext=[".html",".js",".php",""]
	print("[+] URL: ", url)

	# Request Headers
	headers = {
		'User-Agent':'Macintosh Mac OS X'
	}

	#Working with file
	file = open("direnumwordlist.txt",'r')
	lines = file.readlines()

	#Checking if URL schema exists in the url
	if ('http' in url) or ('https' in url):
		pass
	else:
		url="http://"+url
		#print('Please enter a URL Schema')
		#sys.exit()
	dictt={}
	# Parsing through each word in the wordlist
	try:
		for line in lines:
			line = line.strip("\n")
			for i in ext:
				r = requests.get(url+'/'+line+i, headers=headers)
				#print(args.url+'/'+line+i, ":", r.status_code)
				if(r.status_code != 404):
					print("Found :"+url+'/'+line+i, ":", r.status_code)
					a=(url+'/'+line+i)
					dictt[a]=r.status_code
	except:
		print("Error Occured")
	return (dictt)
#direnumm("http://10.0.2.11")