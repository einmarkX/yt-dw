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

from pytube.cli import (
    _ffmpeg_downloader as downloaders,
    _unique_name as fileUnique,
    _download as clidownload
    )
try:
    from pytube import YouTube, Stream, helpers
    


    import ffmpeg
    print(G + "Mantap! Pytube module terinstall!")
except ModuleNotFoundError:
    print(R + "Pytube module gak ada nih! Aku install dulu cuy")
    os.system('pip install pytube &> /dev/null')
    print(G + "Ok siap")
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

class RewriteFunction(object):
    """
    Fungsi ini untuk menulis ulang fungsi-fungsi yang telah disediakan
    """
    def Downloaderffmpeg(
        self, audio_stream: Stream, video_stream: Stream, target: str 
    )-> str:
        video_unique_name = fileUnique(
            helpers.safe_filename(video_stream.title),
            video_stream.subtype,
            "video",
            target=target,
        )

        audio_unique_name = fileUnique(
            helpers.safe_filename(video_stream.title),
            audio_stream.subtype,
            "audio",
            target=target,
        )

        clidownload(stream=video_stream, target=target, filename=video_unique_name)
        print("Loading audio...")
        clidownload(stream=audio_stream, target=target, filename=audio_unique_name)

        video_path = os.path.join(
            target, f"{video_unique_name}.{video_stream.subtype}"
        )
        audio_path = os.path.join(
            target, f"{audio_unique_name}.{audio_stream.subtype}"
        )
        final_path = os.path.join(
            # target, f"{helpers.safe_filename(video_stream.title)}.{video_stream.subtype}"
            target, f"{helpers.safe_filename(video_stream.title)}.mp4"
        )

        try:
            subprocess.run(  
                [
                    "ffmpeg",
                    "-i",
                    video_path,
                    "-i",
                    audio_path,
                    "-codec",
                    "copy",
                    final_path,
                    "-loglevel",
                    "quiet"
                ]
            )
        except:
            print("Ada kesalahan saat menggabungkan video")
            sleep(0.5)
            print("Tapi tenang, file video dan audio masih ada")            
        finally:
            print("File berhasil di didownload")
            print("File disimpan di \n",final_path)

            os.unlink(video_path)
            os.unlink(audio_path)
            return final_path

        return None
            

class DownloadYT(RewriteFunction):
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
        """ Cek apakah link valid atau tidak """
        try:
            if self._isDebug:
                self._link = 'https://www.youtube.com/watch?v=8uy7G2JXVSA'
                return

            tanya = input("Link Youtube: ")
            link = urlparse(tanya)
            
            if not link.scheme :
                raise ValueError("Link Tidak Valid")
            if not (link.netloc == 'www.youtube.com'):
                raise ValueError("Bukan Link Youtube")

            self._link = tanya

        except ValueError as pesan:
            print(pesan)
            self.tanyaLink()
        
    def DownloadVideo(self, tipe):
        prefix_audio = 'audio_'
        prefix_video = 'video_'
        print("Tipe :",tipe)
        
        if tipe == 'Video':
            os.chdir(self._savePath)
            v = "./video_Weird Genius - Lathi (ft Sara Fajira) Official Music Video.mp4"
            a = "./audio_Weird Genius - Lathi (ft Sara Fajira) Official Music Video.mp4"
            
            if (not os.path.exists(v) or not os.path.exists(a)):
                print("File Tidak ditemukan")
                os.close()
            
            i_video = ffmpeg.input(v)
            i_audio = ffmpeg.input(a)

            fusion  = ffmpeg.concat(i_video, i_audio, v=1, a=1).output('./sate.mp4')
            fusion.run()
            
        elif tipe == 'Audio':
            self._Audio.download(self._savePath, filename_prefix="MP3_")
            
            


    @isDebug.setter
    def isDebug(self, isDebug):
        self._isDebug = isDebug
        
    
    def run(self):
        """ Fungsi awal saat program dijalankan """

        if(self._isDebug):
            print("Mode Debug Active")
            
        if self._link is None:
            self.tanyaLink()

        print("Link yang di dapat",self._link)
        
        self._YT = YouTube(self._link)
        self._YT.check_availability
            
        self.infoVideo()
        sleep(3)
        pilihan = self.resolusi()
        print("Pilihan kamu: ", pilihan)
        
        try:
            super(DownloadYT, self).Downloaderffmpeg(self._Audio, self._Video, self._savePath)
        
        except:
            print("Terjadi kesalahan!")
            return
        
        
        

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

        
        

MX = DownloadYT()
MX.run()

