#!/bin/env/python3
#cod UTF-8

#Hecho por J4SH 

#Librerias a Importar:

import os
import requests
import socket
from os import path
import argparse
import sys

#Definicion de los argumentos

parser = argparse.ArgumentParser()

parser.add_argument('-t','--target',help="Indica el dominio victima")
parser.add_argument('-s','--subdominios',action='store_true',help="Encuentra subdominios")
parser.add_argument('-a','--admin',action='store_true',help="Encuentra la el login de admin")
parser.add_argument('-p','--portscan',action='store_true',help="Un simple escaner de puertos" )
parser.add_argument('-sql','--sqlscan',action='store_true',help="Proeba a ver si una pagina es vulnerable a sqlinjection")

args = parser.parse_args()

#Banner

def banner():
    os.system("clear")
    print(" ______       ______  _             _             ")
    print("| ___ \      |  ___|(_)           | |            ")
    print("| |_/ /_   _ | |_    _  _ __    __| |  ___  _ __ ")
    print("|  __/| | | ||  _|  | || '_ \  / _` | / _ \| '__|")
    print("| |   | |_| || |    | || | | || (_| ||  __/| |   ")
    print("\_|    \__, |\_|    |_||_| |_| \__,_| \___||_|   ")
    print("        __/ |                                    ")
    print("       |___/                                     ")
    print("\n\nHECHO POR J4SH\n")

#Encontrador de Subdominios

def admin():
    #Identifica que la wordlist existe
    if path.exists('admin.txt'):
        wordlist_archivo = open('admin.txt','r')
        wordlist = wordlist_archivo.read().split('\n')
        wordlist_archivo.close()
        #Los protocolos se definen
        for protocolo in ("http", "https"):
            #Busca el login en la wordlist
            for admin in wordlist:
                #Define la URL
                url = f"{protocolo}://{args.target}{admin}"
        
                print(f"[+] Probando url '{url}'")
                #Se hace el request a la url a ver si existe
                res = requests.get(url)
                print(f"[!] Respuesta: '{res.status_code}'")
                #Si la respuesta es 200 la pagina existe
                if res.status_code == 200:
                    print("[+] Admin login Descubierto: " + url)
                    break
    else:
        print("[-] Worldist de admin no encontrada!!!")

def subdominios():
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

def escanerpuertos():
    for port in range(1,65536):#en futuro se agregara la opcion de elegir los puertos que se prefieran
        #Se define la conexion TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Se define el tiempo de respuesta
        socket.setdefaulttimeout(0.3)
        result = s.connect_ex((args.target,port))
        #Si es 0 el puerto esta abierto
        if result == 0:
            print(f"[+]El puerto {port} se encuentra abierto")
        s.close()

def sqlscan():
    for protocolo in ("http", "https"):
        url = args.target
        res = request.get(url)
        res2 = request.get(url+"%27")
        print(f"Probando url: {url}")
        
        if res!=res2:
            print(f"[+]La url {url} es vulnerable!!!")
        
        else:
            print("[!]La url no es vulnerable :(")
            break
def main():

    if args.target:
        print("-"*50)
        print(f"| El target es : {args.target}|")
        print("-"*50)

        if args.admin:
            admin()

        elif args.subdominios:
            subdominios()

        elif args.portscan:
            escanerpuertos()

        elif args.sqlscan:
            sqlscan()
    
    else:
        print("\nIMPORTANTE: \n-Usa -h para ver las opciones\n-Solo usar una opcion\n-Escribe la pagina SIN HTTP o HTTPS\n-Por favor usa '/' al final de la url\n-En el escaner de puertos por favor usa la ip\n")
        sys.exit()

if __name__ == '__main__':
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\nSaliendo....")
        sys.exit()
