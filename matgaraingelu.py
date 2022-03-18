import os
import sys
import time

def menu():


    print("+=============================+")
    print("[+] kalkulator script")
    print("[+] author : FarrelHaxor")
    print("+=============================+")
    os.system("figlet Kalkulator")

    menu = input("tentukan operasi yg ingin anda lakukan misalnya +,-,*,/ : ")
    if menu not in("x,+,-,/"):
        print("operasi error silahkan coba lagi")

    y = int(input("\nmasukan angka pertama anda : "))
    x = int(input("masukan angka ke dua anda : "))

    jumlah = y + x
    kali = y * x
    kurang = y - x
    bagi = y / x

    print("", end="\n")
    if "+" in menu:
        print("hasil dari",y,"+",x,"= {}".format(jumlah))

    if "-" in menu:
        print("hasil dari",y,"-",x,"= {}".format(kurang))

    if "/" in menu:
        print("hasil dari",y,"/",x,"= {}".format(bagi))

    if "*" in menu:
        print("hasil dari",y,"*",x,"= {}".format(kali))

menu()

