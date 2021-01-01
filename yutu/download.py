from ffmpeg import RewriteFunction
from pytube import YouTube
from urllib.parse import urlparse, parse_qs

from helpers import ceksize, pilihAngka
from logs import Logs
from warna import prCyan

import time
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
        
    def garis(self)->str:
        return("========================================")
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

    @isDebug.setter
    def isDebug(self, isDebug):
        self._isDebug = isDebug
        
    
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
    

            
    

    
    def resolusi(self):
        yts = self._YT.streams
        yt_video = yts.filter(type='video')
        yt_audio = yts.get_audio_only()
        jumlahpilihan = len(yt_video) + 1
        
        print("{0:2} {1:10} {2}".format('No', 'Resolusi', 'Size'))
        for i,data in enumerate(yt_video, start=1):
            resolusi = data.resolution
            print("{0:2} {1:10} {2}".format(i, resolusi, ceksize(data.filesize) ))

        print("{0:2} {1:10} {2}".format(len(yt_video)+1,"Audio MP3", ceksize(yt_audio.filesize)))
        print(self.garis())
        strpilih = "Pilih Nomor 1 sampai {0} : ".format(str(jumlahpilihan) )

        pilih = pilihAngka(strpilih)
        
        if ((pilih) > jumlahpilihan):
            print("Pilihan Tidak Valid")
            self.resolusi()

        self._Audio = yt_audio
        
        
        if ( (pilih) == jumlahpilihan):
            return "audio"

        self._Video = yt_video[pilih-1]
        return "video"

    def run(self):
        """ Fungsi awal saat program dijalankan """

        if(self._isDebug):
            print("Mode Debug Active")
            
        if self._link is None:
            self.tanyaLink()
        
        self._YT = YouTube(self._link)
        self._YT.check_availability
        
        self.infoVideo()
        time.sleep(3)
        pilihan = self.resolusi()
        
        cek = Logs()
        cek.run()

        self._savePath = cek._path
        print("Jenis file ", prCyan(pilihan))
        try:
            if pilihan == 'video':
                super(DownloadYT, self).Downloaderffmpeg(self._Audio, self._Video, self._savePath)
            elif (pilihan == 'audio'):
                super(DownloadYT, self).DownloadMP3(self._Audio, self._savePath)
            else:
                raise ValueError("Error")
        except:
            print("Terjadi kesalahan!")
            return
        
        