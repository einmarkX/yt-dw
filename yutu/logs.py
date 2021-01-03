import configparser
import os
from warna import prRed, prGreen, prCyan
from helpers import s

class Logs:
    """
    berhubungan dengan config.ini
    """

    def __init__(self, development = True):
        
        self._isValidPath: bool = False
        self._path:str = None
        self._config = None
        self._lokasiconfig = "./yutu/config/config.ini"
    
    def cek(self)-> bool:
        config = configparser.ConfigParser()
        try:
            if not os.path.exists(self._lokasiconfig):
                raise Exception("Config.ini tidak ditemukan")

            config.read(self._lokasiconfig)
            self._config = config['DEFAULT']


            if not (config['DEFAULT']['path']):
                raise Exception("Default Path Config tidak ditemukan")
            
            if not os.path.isdir(config['DEFAULT']['path']):
                raise Exception("Lokasi penyimpanan belum ditentukan ")
                return False

            self._path = config['DEFAULT']['path']
            self._isValidPath = True

        except Exception as Pesan:
            print(s("Error: %s" %(prRed(Pesan))))
            self._isValidPath = False
            return False
        
        return True
    def simpanPath(self):
        pilih = (input("Masukkan folder tempat menaruh hasil download : "))
        if not os.path.isdir(pilih):
            raise Exception("{0} Bukanlah sebuah folder".format(pilih))

        config = configparser.ConfigParser()
        config.read(self._lokasiconfig)
        config.set('DEFAULT','path', pilih)

        with open(self._lokasiconfig, 'w') as configfile:
            config.write(configfile)

        print(s("Default Lokasi download sudah diganti ke "))
        print(s(prGreen(pilih)))

    def gantiPath(self):
        try:
            pilih = (input(s("Apakah ingin menggantinya ? opsi (y/t) ")))
            if pilih == 'y' or pilih  == 'Y':
                self.simpanPath()
                
            
        except Exception as Pesan:
            print(s("Error: %s" %(prRed(Pesan))))
            self.gantiPath()

        


    def run(self):
        # print(s("Running..")
        self.cek()
        if(self._isValidPath):
            print(s("Lokasi penyimpanan ditemukan di: " ))
            print(s("%s" %(prGreen(self._path))))
            print("")
            self.gantiPath()
        else:
            self.simpanPath()
        

        

        
