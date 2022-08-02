import requests
from colorama import Fore,init
from os import system
from time import sleep
from sys import platform
if platform == 'linux':
    system('clear')
else:
    system('cls')
init(autoreset=True)
red = Fore.RED
yellow = Fore.YELLOW
blue = Fore.BLUE
green = Fore.GREEN
cyan = Fore.CYAN
reset = Fore.RESET
pur = "\033[35m"

rr = requests.session()
print(f'''
{pur}
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░██░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░▄▄███▄░░░░░▒▒▒▒▒▒▒▒▒
▒▒▒▒░░░░░░░░░░░░▐██▌░░░░░░░▒▒▒▒▒▒▒▒
▒▒▒░░░░░░░░░░░░░░▀█░░░░░░░░░▒▒▒▒▒▒▒
▒▒░░░░░░░░░░░░░░▄███░░░░░░░░░▒▒▒▒▒▒
▒░░░░░░░░░░░░░░░████░░░░░░░░░░▒▒▒▒▒
▒░░░░▄░░░░░░░░░▐████░░░░░░░░░░▒▒▒▒▒
▒░░░░░▀▀▄░░░░▄█▀░███░░░░░░░░░░▒▒▒▒▒
▒░░░░░░░░▀▀█▀░░░░▐███░░░░░░░░░▒▒▒▒▒
▒▒░░░░░░░░░░▀▄▄▄▄████▌░░░░░░░▒▒▒▒▒▒
▒▒▒░░░░░░░░░██████████░░░░░░▒▒▒▒▒▒▒
▒▒▒▒░░░░░░░░░█████████░░░░░▒▒▒▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░▀██████░▀▄░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░▀████▄░▀▀▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▀██▄▒▒▒▀▄▄▄▄▄▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀█▄▒▒▒▒███▄▀█
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀███▀▀
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▒


    
{reset}

c o d e d bY {pur}A Z O {reset}| {pur}insta {reset}: {pur}r7jhz1 {reset}| {pur}snapchat {reset}: {pur}uur_2v {reset}| {pur}github {reset}: {pur}az0122 {reset}{pur}</3 {reset}


    ''')

def s():   
    global ii,url
    ii = input(f'{yellow}IP address {red}?{reset} : ')
    url = (f"https://api.secretprojects.xyz/v1/geoip/?ip={ii}")
    if len(ii) < 5:
        print('')
        print(f'{red}wrong IP [!] {reset}')
        print('')
        s()
    
s()
print('')

r = rr.get(url)

if ('"status":false,"message":"IP Address Is Invalid"') in r.text:
    print('')
    print(f'{red}wrong IP [!] {reset}')
    print('')
    sleep(3)
    s()

requests = requests.get(url)
print(f'{green}{requests.text}')