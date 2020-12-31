#!/usr/bin/env python


#Made BY M24-py
#Feature By NamakuHendra
#Fix By jabbarbie 
#Thanks !

from urllib.parse import urlparse, parse_qs
import subprocess

import os,sys,time,os.path
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
try:
    import pytube
    from pytube import YouTube

    import ffmpeg
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

class DownloadYT():
    def __init__(self, isDebug=False):
        """ Constructor 
        :param boolean debug:
            untuk mengecek dalam mode pengembang atau tidak
            jika true, skip semua banner / animasi
        """

        self._isDebug: bool = isDebug
        self._link = None
        self._isPlaylist: bool = False
        self._YT = YouTube
        self._savePath = 'D:/b'
        
        

    @property
    def isDebug(self):
        """Get Mode"""
        return self._isDebug

    @property
    def link(self):
        """Link Video yang akan didownload"""
        return self._link

    """
    @link.setter
    def link(self, link):
        self._link = link;
    """

    @link.setter
    def YT(self, YT):
        print("Dibuat")
        self._YT = YT
        
    def tanyaLink(self):
        if self._isDebug:
            self._link = 'https://www.youtube.com/watch?v=8uy7G2JXVSA'
            return
        link = urlparse(input("Link Youtube: "))
        #print(link)

        if link.netloc is None:
            print("Link Tidak Valid")
            self.tanyaLink()
        if not (link.netloc == 'www.youtube.com'):
            print("Bukan Link Youtube")
            self.tanyaLink()
        self._link = link


        self._Audio = None
        self._Video = None
        
    def DownloadVideo(self, tipe):
        prefix_audio = 'audio_'
        prefix_video = 'video_'
        print("Tipe :",tipe)
        
        if tipe == 'Video':

            #v = self._Video.download(self._savePath, filename_prefix=prefix_video)
            #a = self._Audio.download(self._savePath, filename_prefix=prefix_audio)

            
            #input_video = ffmpeg.input(v)
            #input_audio = ffmpeg.input(a)
            #in_file = input_video
            #print(v)
            #print(a)
            
            
            #os.chdir(self._savePath)
            #print(ffmpeg)
            #ffmpeg.concat( input_video.trim(start_frame=10, end_frame=20), input_video.trim(start_frame=30, end_frame=40)).output('./satekambing.mp4').run()

            os.chdir(self._savePath)
            v = "./video_Weird Genius - Lathi (ft Sara Fajira) Official Music Video.mp4"
            a = "./audio_Weird Genius - Lathi (ft Sara Fajira) Official Music Video.mp4"
            
            if (not os.path.exists(v) or not os.path.exists(a)):
                print("File Tidak ditemukan")
                os.close()
                
            print(v)
            subprocess.run(
                [
                    "php",
                    "-i",
                    v,
                    "-i",
                    a,
                    "-codec",
                    "copy",
                    "./sate.mp4"
                ]
            )
            """
            i_video = ffmpeg.input(v)
            i_audio = ffmpeg.input(a).audio.filter('adelay', "1500|1500")

            merge_iaudio = ffmpeg.filter([i_video, i_audio], 'amix')

          

    
            """
            """
            return
            proses = (
                ffmpeg
                .concat(i_video, merge_iaudio, v=1, a=1)
                .output("./mix_delay.mp4")
                .overwrite_output()
                .run_async(pipe_stdin=True)
            )
            out, err = proses.communicate()
            
            
            fusion  = ffmpeg.concat(i_video, i_audio, v=1, a=1).output('./sate')
            fusion.run()
            print(fusion)
            #.output('jadi.mp4').run()
           """
        elif tipe == 'Audio':
            self._Audio.download(self._savePath, filename_prefix="MP3_")
            
            


    @isDebug.setter
    def isDebug(self, isDebug):
        self._isDebug = isDebug
        
    
    def run(self):

        """
        if(self._isDebug):
            print("Mode Debug Active")
            
        if self._link is None:
            self.tanyaLink()

        self._YT = YouTube(self._link)
        self._YT.check_availability
            
        self.infoVideo()
        pilihan = self.resolusi()
        print("Pilihan kamu: ", pilihan)
        
        self.DownloadVideo(pilihan)
        """
        self.DownloadVideo('Video')
        

    def garis(self) -> str:
        return "===================================="
    
    def infoVideo(self):
        """Menampilkan Informasi Video"""
        
        print(self.garis())
        print("Judul\t:",self._YT.title)
        print("View\t:",self._YT.views)
        print("Rating\t:",self._YT.rating)

        print("Publish\t:",self._YT.publish_date)
        print("Durasi\t: {0} Menit".format(self._YT.length / 60))
        print("Chanel\t:",self._YT.author)
        
        print(self.garis())
                        
    def download():
        print("")


            
    def ceksize(self, filesize: 0) -> str:
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
        
    def pilihAngka(self, tanya)-> int:
        try:
            pilih = int(input(tanya))
        except ValueError:
            print("Input Invalid")
            pilihAngka(tanya)

        return pilih
    
    def resolusi(self):
        yts = self._YT.streams
        yt_video = yts.filter(type='video')
        yt_audio = yts.get_audio_only()
        jumlahpilihan = len(yt_video) + 1
        
        print("{0:2} {1:10} {2}".format('No', 'Resolusi', 'Size'))
        for i,data in enumerate(yt_video, start=1):
            resolusi = data.resolution
            print("{0:2} {1:10} {2}".format(i, resolusi, self.ceksize(data.filesize) ))

        print("{0:2} {1:10} {2}".format(len(yt_video)+1,"Audio MP3", self.ceksize(yt_audio.filesize)))
        print(self.garis())
        
        strpilih = "Pilih Nomor 1 sampai {0} : ".format(str(jumlahpilihan) )

        pilih = self.pilihAngka(strpilih)
        
        if ((pilih) > jumlahpilihan):
            print("Pilihan Tidak Valid")
            self.resolusi()

        self._Audio = yt_audio
        
        
        if ( (pilih) == jumlahpilihan):
            return "Audio"

        self._Video = yt_video[pilih-1]
        return "Video"

        
        
        
        
        
    def download2():
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

    
    def pilihvideo():
        save_path = "D:/b"
        yt = YouTube("https://www.youtube.com/watch?v=8uy7G2JXVSA")
        
        yts = yt.streams
        yt_video = yts.filter(type='video')
        yt_audio = yts.get_audio_only()

        print(str(yt_video.first().default_filename()))
        
        print("\n" + Y + "{0:2} {1:10} {2}".format('No', 'Resolusi', 'Size'))

        
        for i,data in enumerate(yt_video, start=1):
            resolusi = data.resolution
            print(W + " {0:2} {1:10} {2}".format(i, resolusi, ceksize(data.filesize)))
        
        print(W + " {0:2} {1:10} {2}".format(len(yt_video)+1,"MP3", ceksize(yt_audio.filesize)))

        yt_audio.download(output_path=save_path ,filename_prefix='audio_')
        #yt_video.download(output_path=save_path, filename_prefix='video_')
        #os.chdir(save_path)
        
        strpilih = input("\n" + G + "Pilih Nomor 1 sampai {0} > ".format(str(len(yts)) ))
        
        try:
            pilihint = int(strpilih) - 1
            if (pilihint >= (len(yts)+1) ):
                raise ValueError()

            vt_video_pilih = yt_video[pilihint]
            os.chdir(save_path)
            print(vt_video_pilih.default_filename())
            
            #vt_video_pilih.download(output_path=save_path, filename_prefix='video_')
            
     #       i_video = ffmpeg.input("video_".vt_video_pilih.filename)
     #       i_audio = ffmpeg.input("audio_".vt_audio.filename)
            
            #ffmpeg.concat(i_video, i_audio, v=1, a=1).output(yt_video_filename).run()
    #       return yts[pilihint]
            
        except ValueError:
            print(R + "Pilihan Tidak Valid")
            pilihvideo()


    #

MX = DownloadYT(True)
MX.run()

