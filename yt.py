#!/usr/bin/env python


#Made BY M24-py 
import os,sys,time,os.path
try:
    import pytube
    from pytube import YouTube
    print("Mantap! Pytube module terinstall!")
except ModuleNotFoundError:
    print("Pytube module gak ada nih! Aku install dulu cuy")
    os.system('pip install pytube &> /dev/null')
    print("Ok siap")
from time import sleep
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
banner = """
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{}
__   _______   
\ \ / /_   _| 
 \ V /  | |   
  | |   | |   v1.2-2 Stable 
  |_|   |_|   Downloader 

{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{}
"""
banmer = """

1 > Download Video Youtube    96 > Keluar 

2 > Tentang 

"""
def about():
    os.system("clear")
    sleep(0.5)
    print(Y + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sleep(0.1)
    print("")
    print(G + "Made By M24-Cheems 100%") 
    print("")
    sleep(0.1)
    print(Y + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    bckmenu()
def cheems():
    os.system("clear")
    sleep(0.5)
    print(W + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sleep(0.1)
    print(Y + "Cheems M24")
    sleep(0.1)
    print(W + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 
    sleep(2.5)
    os.system("clear") 
def bckmenu():
    menu()
def download():
    os.system("clear")
    sleep(1)
    print(banner)
    print("")
    sleep(0.1)
    link = str(input(G + "Link Youtube •> "))
    yt = YouTube(link)
    lod = "\|/-\|/-"
    for i in range(110):
        sleep(0.1)
        sys.stdout.write("\r" + lod[i % len(lod)])
        sys.stdout.flush()
    os.system("clear")
    sleep(1.4)
    print(banner)
    sleep(0.1)
    print(G + "Judul •> " ,yt.title)
    sleep(0.1)
    print(G + "Views •> ",yt.views)
    sleep(0.2)
    print(G + "Rating •> ", yt.rating)
    sleep(1.5)
    dl = str(input(W + "Download Ke > "))

    ys = yt.streams.get_highest_resolution()
    if (os.path.isdir(dl)):
        print( Y + "Memulai Download.....")
        ys.download(dl)
    else:
        print(R + "[!] Direktori Tidak ada")
    print(G + "Selesai ! ")
    sleep(1.5)
    bckmenu()

    
def menu():
    animation = "\|/-\|/-"
    for i in range(115):
        sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    os.system("clear")
    sleep(1.5)
    print(Y + banner)
    sleep(0.1)
    print(G + banmer)
    inp = str(input(G + "> "))
    if inp == "1":
        download()
    elif inp == "2": 
        about()
    elif inp == "96":
        cheems()
    else:
        print(R + "Pilihan Invalid")
menu() 
#
