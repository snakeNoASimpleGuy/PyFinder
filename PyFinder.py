#Hecho por J4SH como parte del ejercicio de mi curso
#Si hay derechos de autor por el name sorry :(
import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-t','--target',help="Indica el dominio victima")
parser.add_argument('-s','--subdominios',action='store_true',help="Encuentra subdominios")
parser.add_argument('-a','--admin',action='store_true',help="Encuentra la el login de admin")

args = parser.parse_args()

def banner():
    print("______       ______  _             _             ")
    print("| ___ \      |  ___|(_)           | |            ")
    print("| |_/ /_   _ | |_    _  _ __    __| |  ___  _ __ ")
    print("|  __/| | | ||  _|  | || '_ \  / _` | / _ \| '__|")
    print("| |   | |_| || |    | || | | || (_| ||  __/| |   ")
    print("\_|    \__, |\_|    |_||_| |_| \__,_| \___||_|   ")
    print("        __/ |                                    ")
    print("       |___/                                     ")
    print("\n\nHECHO POR J4SH\n\n")

def main():
    if args.target:
        print(f"\n\nLa pagina es:  {args.target}\n ")

    if args.admin:
        if path.exists('admin.txt'):
            wordlist = open('admin.txt','r')
            wordlist = wordlist.read().split('\n')

            for admin in wordlist:
                url = "http://"+admin+"."+args.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("[+] Admin login Descubierto: " + url)

            for admin in wordlist:
                url = "https://" + admin + "." + args.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("[+] Admin login Descubierto: " + url)

    if args.subdominios:
        if path.exists('subdominios.txt'):
            wordlist = open('subdominios.txt','r')
            wordlist = wordlist.read().split('\n')

            for subdominio in wordlist:
                url = "http://"+subdominio+"."+args.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("[+] Subdominio Descubierto: " + url)

            for subdominio in wordlist:
                url = "https://" + subdominio + "." + args.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("[+] Subdominio Descubierto: " + url)

    else:
        print("\n\nPor favor usa '-h' para ver las opciones")
        sys.exit()

if __name__ == '__main__':
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\nSaliendo....")
        sys.exit()
