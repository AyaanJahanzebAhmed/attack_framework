#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import platform
import webbrowser
import requests


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Darwin':
        os.system('clear')
    else:
        os.system('clear')


def main():
    clear()
    print("""

\tTab 1 Directory Listing
\tTab 2 Configuration Files
\tTab 3 Database Files
\tTab 3 Log Files
\tTab 4 Backup and Old Files
\tTab 5 Login Pages
\tTab 6 SQL Errors
\tTab 7 Publicly Exposed Documents
\tTab 8 phpinfo()
\tTab 9 Google Hacking Database)""")
    webbrowser.open_new_tab(google_hacking + 'site:' + url + '+intitle:index.of')
    webbrowser.open_new_tab(
        google_hacking + 'site:' + url + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini')

    webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:sql+|+ext:dbf+|+ext:mdb')
    webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:log')
    webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup')
    webbrowser.open_new_tab(
        google_hacking + 'site:' + url + '+inurl:login | admin | user | cpanel | account | moderator | /cp')
    webbrowser.open_new_tab(
        google_hacking + 'site:' + url + '+intext:"sql+syntax+near"+|+intext:"syntax+error+has+occurred"+|			+intext:"incorrect+syntax+near"+|+intext:"unexpected+end+of+SQL+command"+|+intext:"Warning:+mysql_connect()"+|+intext:"Warning:+mysql_query()"+|+intext:"Warning:+pg_connect()"')
    webbrowser.open_new_tab(
        google_hacking + 'site:' + url + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv')
    webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:php+intitle:phpinfo+"published+by+the+PHP+Group"')
    webbrowser.open_new_tab('https://www.exploit-db.com/google-hacking-database/')


if __name__ == '__main__':
    clear();
    print('\n[#] - Checking Modules...')
    try:
        import requests

        print('[+] - requests == OK!')
    except ImportError:
        raise ImportError('\n[!] - requests == NOT OK!')
    print('\n[#] - Checking URL...')
    try:
        url = sys.argv[1]
        print('[+] - URL == OK!')
        print('URL: ' + url)
    except IndexError:
        print('[!] - URL == NOT OK!')
        url = str(input('URL: '))
    if 'http://' not in url:
        hostname = url
        print('[+] - URL == Adding http://')
        url = ('http://' + url)
        print('URL: ' + url)
    elif 'http://' in url:
        hostname = url.replace('http://', '')
        url = url
    print('[+] - Search Engine == SET!')
    google_hacking = 'https://www.google.com/search?q='
    main()