#!$PREFIX/bin/bash


#############################################################
#############################################################
#******************************##############################
#*Dibuat Oleh : M24-XT        *##############################
#*Setup Installer Untuk       *##############################
#*Program Youtube Downloader  *##############################
#******************************##############################
#############################################################
#############################################################
#***********************************************************#
# Kontributor & Pembuat Program Ini,& Youtube Downloader:   #
# - https://github.com/M24-XT                               #
# - https://github.com/jabbarbie                            #
# - https://github.com/NamakuHendra                         #
# Program Ini Dibawah Lisensi GNU GPL v3                    #
#***********************************************************#
#############################################################
#Start 
W='\033[1;37m'
Y='\033[1;33m'
R='\033[1;31m'
G='\033[1;32m'
B='\033[1;34m'
os=`echo $OSTYPE`
#
ins(){
	clear
	sleep 1
	apt-get update
	apt-get upgrade
	apt-get install ffmpeg
	clear
	sleep 0.5
	echo $W ------------------------------------------------------------
	sleep 0.1
	echo 
	echo $G [✓] Selesai !
	echo
	sleep 0.1
	echo $W ------------------------------------------------------------
	sleep 0.1
	echo $Y [*] Menjalankan YT Downloader.........
	sleep 2.6
	python yutu


}
main_setup(){
	clear
	sleep 1.5
	echo $W ------------------------------------------------------------
	sleep 0.1
	echo 
	echo $G Setup Untuk Program Youtube Downloader V1.2.7
	echo 
	sleep 0.1
	echo $W ------------------------------------------------------------
	echo
	sleep 0.1
	echo $Y [•] Sabar......
	sleep 2
	ins
}
pass(){
	clear
	sleep 1
	echo $W ------------------------------------------------------------
	sleep 0.1
	echo
	echo $G [✓] Tidak Perlu Setup 
	echo
	sleep 0.1
	echo $W ------------------------------------------------------------
	echo
	sleep 0.5
	echo $Y [*] Menjalankan YT Downloader......
	sleep 2.5
	python yutu
}
if [ $os==linux-android ]
then
	bin_directory=/data/data/com.termux/files/usr/bin
	if [ -f $bin_directory/ffmpeg ] && [ -f $bin_directory/python ]
	then
		pass
	else
		main_setup
			
	fi
elif [ $os==linux-gnu ]
then
	bin_directory=/usr/bin
	if [ -f $bin_directory/ffmpeg ] && [ -f $bin_directory/python ]
	then
		pass
	else
		main_setup
	fi
else
	echo $R OS tidak Diketahui, Atau Belum Di support
fi
