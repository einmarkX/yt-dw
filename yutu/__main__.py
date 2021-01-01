import sys
import time
from urllib.parse import urlparse, parse_qs

from download import DownloadYT
from helpers import pilihAngka
from warna import prRed, prCyan, prYellow
from logs import Logs
from banner import Banner
from version import __constributor__

def main(bukaBanner = True):

    # Banner
    if bukaBanner:
        B = Banner(True)
        B.cetakbanner()
        B.menu()

    try:
        pilih = pilihAngka("Pilih Menu : ")
        if (pilih > 4):
            raise Exception("Menu yang dipilih tidak ada! ")

        # switch case ribet di python.. if aja :D
        if (pilih == 1):
            # download
            DLYt = DownloadYT(False)
            DLYt.run()
            time.sleep(5)

        elif (pilih == 2):
            # ganti save path
            cek = Logs(True)
            cek.cek()
            cek.run()
        elif pilih == 3:
            # about
            print(prYellow("Team Programmer & Contributor :"))
            for nama in __constributor__:
                print("- ",prCyan(nama))
        else:
            # exit
            sys.exit(prCyan("Terima kasih! ;) "))
           
    except Exception as Pesan:
        print("Error ", prRed(Pesan))
    
    main(False)


main()

        
        

# MX = DownloadYT()
# MX.run()

