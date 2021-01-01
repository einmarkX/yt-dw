from banner import Banner
from urllib.parse import urlparse, parse_qs

from download import DownloadYT

# Banner
B = Banner(True)
B.cetakbanner()
B.menu()

DLYt = DownloadYT(False)
DLYt.run()

 

        
        

# MX = DownloadYT()
# MX.run()

