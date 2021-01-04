from warna import *
from version import __version__
from helpers import s
class Banner:
    """ Hanya untuk menampilkan Banner """
    
    def __init__(self, show = True):

        self._debug = show

    def cetakbanner(self) :
        print (prRed("""
    __   ________   
    \ \ / /_   _| 
     \ V /  | |  
      | |   | |  _  {1}Versi {0}
      |_|   |_| |_| Downloader 
    """.format(prGreen(__version__), prEnd() )))

    def menu(self): 
        print ("""
  1 > Download Video Youtube     
  2 > Ubah Penyimpanan Video 
  3 > Tentang
  4 > Keluar
        """)
