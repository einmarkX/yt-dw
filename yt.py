#!/usr/bin/env python


#Made BY M24-py
#Feature By NamakuHendra
#Fix By jabbarbie 
#Thanks ! 
import os,sys,time,os.path
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
try:
    import pytube
    from pytube import YouTube
    print(G + "Mantap! Pytube module terinstall!")
except ModuleNotFoundError:
    print(R + "Pytube module gak ada nih! Aku install dulu cuy")
    os.system('pip install pytube &> /dev/null')
    print(G + "Ok siap")
    import pytube
    from pytube import YouTube

from time import sleep
banner = """
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{}
__   _______   
\ \ / /_   _| 
 \ V /  | |   
  | |   | |   v1.4-4 Stable
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
    print(G + "Thanks To NamakuHendra,jabbarbie for fixing ! ") 
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
    print(Y + "Thanks To NamakuHendra,jabbarbie for fixing ! ")
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

    ys = pilihvideo(yt)

    dl = str(input(W + "Download Ke > "))
    
    if (os.path.isdir(dl)):
        print( Y + "Memulai Download.....")
        ys.download(dl)
    else:
        print(R + "[!] Direktori Tidak ada")
    sleep(1)                                                        
    os.system("clear")
    print(banner)
    conv = str(input(Y + "[?] Convert Ke MP3 (Y/t) "))
    if conv == "Y":
        os.chdir(dl)
        oldn = yt.title + '.mp4'
        oldn_v2 = yt.title + '.webm'
        newn = yt.title + '.mp3'
        lz = os.path.isfile(oldn)
        xz = os.path.isfile(oldn_v2)
        if lz==True:
            os.rename(oldn,newn)
            print(G + "[✓] Sukses")
        elif xz==True:
            os.rename(oldn_v2,newn)
            print(G + "[✓] Sukses")
        else:
            print(R + "[!] File Tidak Ada ")
            print(R + "[!] Gagal ")
        
    elif conv == "t":                                           
       print(G + "[*] Ok ! ")
    else:
        print(R + "[!] Pilihan Invalid ")
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

def ceksize(filesize: 0):
    """ parameter : int (byte) """
    ukuran = "bit"
    if (filesize < 1000):
        ukuran = "byte"
        filesize = (filesize/1000)
    elif (filesize < 1000000):
        ukuran = "kB"
        filesize = (filesize/100000)
    elif (filesize >= 1000000):
        ukuran = "MB"
        filesize = (filesize/1000000)

    return "{0:.1f} {1}".format(filesize, ukuran)


def pilihvideo(yt):
    yts = yt.streams.filter().order_by('filesize')
    print("\n" + Y + "{0:2} {1:10} {2}".format('No', 'Resolusi', 'Size'))
    
    for i,data in enumerate(yts, start=1):
        resolusi = data.resolution
        if (data.type == 'audio'):
            resolusi = 'Audio'
        print(W + "{0:2} {1:10} {2}".format(i, resolusi, ceksize(data.filesize)))

    strpilih = "\n" + G + "Pilih Nomor 1 sampai {0} > ".format(str(len(yts)) )
    pilih= (input(strpilih))

    try:
        pilihint = int(pilih) - 1
        if (pilihint > len(yts)):
            raise ValueError()
        return yts[pilihint]
        
    except ValueError:
        print(R + "Pilihan Tidak Valid")
        pilihvideo()


#
menu()
