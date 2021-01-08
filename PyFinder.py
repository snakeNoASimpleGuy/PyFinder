#Hecho por J4SH como parte del ejercicio de mi curso
#Si hay derechos de autor por el name sorry :(
import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Indica el dominio de la victima")
parser = parser.parse_args()

def menu():
    print("PyFinder\nSi me falta un banner pero pa despues\n\n#Hecho por J4SH")
menu()

def main():
    if parser.target:
        if path.exists('subdominios.txt'): #el subdominios.txt puedes cambiarlo por cualquier otro diccionario en github hay mas :)
            wordlist = open('subdominios.txt','r')
            wordlist = wordlist.read().split('\n')

            for subdominio in wordlist:
                url = "http://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("[*]Subdominio encontrado " + url)
            for subdominio in wordlist:
                url = "https://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("[*]Subdominio encontrado " + url)
    else:
        print("Por favor usa un subdominio valido")
        sys.exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo....")
        sys.exit()
