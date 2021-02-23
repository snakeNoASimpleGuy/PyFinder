#Hecho por J4SH 
import os
from os import path
import requests
import socket
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-t','--target',help="Indica el dominio victima")
parser.add_argument('-s','--subdominios',action='store_true',help="Encuentra subdominios")
parser.add_argument('-a','--admin',action='store_true',help="Encuentra la el login de admin")
parser.add_argument('-p','--portscan',action='store_true',help="Un simple escaner de puertos" )

args = parser.parse_args()

def banner():
    os.system("clear")
    print("______       ______  _             _             ")
    print("| ___ \      |  ___|(_)           | |            ")
    print("| |_/ /_   _ | |_    _  _ __    __| |  ___  _ __ ")
    print("|  __/| | | ||  _|  | || '_ \  / _` | / _ \| '__|")
    print("| |   | |_| || |    | || | | || (_| ||  __/| |   ")
    print("\_|    \__, |\_|    |_||_| |_| \__,_| \___||_|   ")
    print("        __/ |                                    ")
    print("       |___/                                     ")
    print("\n\nHECHO POR J4SH\n")

def admin():
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
        print("[-] Worldist de admin no encontrada!!!")

def escanerpuertos():
    for port in range(1,65536):#en futuro se agregara la opcion de elegir los puertos que se prefieran
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.3)
        result = s.connect_ex((args.target,port))
        if result == 0:
            print(f"[+]El puerto {port} se encuentra abierto")
        s.close()

def subdominios():
    if args.subdominios:
        if path.exists('subdominios.txt'):
            wordlist_archivo = open('subdominios.txt','r')
            wordlist = wordlist_archivo.read().split('\n')
            wordlist_archivo.close()

            for protocolo in ("http", "https"):
                for subdominios in wordlist:
                    url = f"{protocolo}://{args.target}{subdominios}"

                    print(f"[+] Probando url '{url}'")

                    res = requests.get(url)
                    print(f"[!] Respuesta: '{res.status_code}'")

                    if res.status_code == 200:
                        print("[+] Subdominio Descubierto: " + url)
                        break
            else:
                print("[-] Wordlist de subdominios no encontrada!!!")

def main():

    if args.target:
        print("-"*50)
        print("El target es : " + args.target)
        print("-"*50)

        if args.admin:
            admin()

        if args.subdominios:
            subdominios()

        if args.portscan:
            escanerpuertos()
    else:
        print("\nIMPORTANTE: \n-Solo usar una opcion\n-Escribe la pagina SIN HTTP o HTTPS\n-Por favor usa '/' al final de la url, exepto en es escaner de puertos\n")
        sys.exit()

if __name__ == '__main__':
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\nSaliendo....")
        sys.exit()
