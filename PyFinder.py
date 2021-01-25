#Hecho por J4SH 
import os
import requests
from os import path
import argparse
import sys

def banner():
    os.system("clear")
         rint("______       ______  _             _             ")
    print("| ___ \      |  ___|(_)           | |            ")
    print("| |_/ /_   _ | |_    _  _ __    __| |  ___  _ __ ")
    print("|  __/| | | ||  _|  | || '_ \  / _` | / _ \| '__|")
    print("| |   | |_| || |    | || | | || (_| ||  __/| |   ")
    print("\_|    \__, |\_|    |_||_| |_| \__,_| \___||_|   ")
    print("        __/ |                                    ")
    print("       |___/                                     ")
    print("\n\nHECHO POR J4SH ayudado por: m3nth0l4thum gracias panita :3\n\n")

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t','--target',help="Indica el dominio victima")
    parser.add_argument('-s','--subdominios',action='store_true',help="Encuentra subdominios")
    parser.add_argument('-a','--admin',action='store_true',help="Encuentra la el login de admin")

    args = parser.parse_args()


    if args.target:
        print(f"\n\nLa pagina es:  {args.target}\n ")

        if args.admin:
            if path.exists('admin.txt'):
                wordlist_archivo = open('admin.txt','r')
                wordlist = wordlist_archivo.read().split('\n')
                wordlist_archivo.close()

                for protocolo in ("http", "https"):
                    for admin in wordlist:
                        url = f"{protocolo}://{args.target}{admin}"

                        print(f"[+] Probando url '{url}'")

                        res = requests.get(url)
                        print(f"[!] Respuesta: '{res.status_code}'")

                        if res.status_code == 200:
                            print("[+] Admin login Descubierto: " + url)
                            break
            else:
                print("[-] Worldist de admin no encontrada")

        if args.subdominios:
            if path.exists('subdominios.txt'):
                wordlist = open('subdominios.txt','r')
                wordlist = wordlist.read().split('\n')
                wordlist_archivo.close()

                for subdominio in wordlist:
                    url = "http://"+subdominio+"."+args.target
                    print(url)
                    try:
                        requests.get(url)
                    except requests.ConnectionError:
                        pass
                    else:
                        print("[+] Subdominio Descubierto: " + url)

                for subdominio in wordlist:
                    url = "https://" + subdominio + "." + args.target
                    print(url)
                    try:
                        requests.get(url)
                    except requests.ConnectionError:
                        pass
                    else:
                        print("[+] Subdominio Descubierto: " + url)

        else:
            print("\nPor favor usa '-h' para ver las opciones\nIMPORTANTE: \n-Solo usar una opcion\n-Escribe la pagina SIN HTTP o HTTPS\n-Por favor usa '/' al final de la url")
            sys.exit()

if __name__ == '__main__':
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\nSaliendo....")
        sys.exit()
