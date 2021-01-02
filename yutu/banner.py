from warna import *
from version import __version__

class Banner:
    """ Hanya untuk menampilkan Banner """
    
    def __init__(self, show = True):

        self._debug = show

    def cetakbanner(self) :
        print ("""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       __   ________   
       \ \ / /_   _| 
        \ V /  | |  
         | |   | |  _  Versi {}
         |_|   |_| |_| Downloader 

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """.format(prGreen(__version__)))

    def menu(self): 
        print ("""
    1 > Download Video Youtube    4 > Keluar 
    2 > Ubah Penyimpanan Video 
    3 > Tentang
        """)
