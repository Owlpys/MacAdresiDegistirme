
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC DEGISTIRME")

print("""\033[94m

MAC ADRES DEGISTIRME ARACINA HOS GELDIN KANKA


1)MAC Adresi Karısık Belirle
2)MAC Adresi Orjinale Haline Getir

""")

owl = input("Secsene Bir Tanesini     : ")

 

if(owl=="1"):
    os.system("ifconfig wlan0 down ")
    os.system("ifconfig eth0 down ")
    os.system("macchanger -r wlan0")
    os.system("macchanger -r eth0 ")
    os.system("ifconfig wlan0 up ")
    os.system("ifconfig eth0 up ")
    print("\033[97mYeni Mac Adresin Hazır Kanka Senin icin Degistirdim Ben :)")
	


elif(owl=="2"):
    os.system("ifconfig wlan0 down ")
    os.system("ifconfig eth0 down ")
    os.system("macchanger -p eth0 ")
    os.system("macchanger -p wlan0 ")
    os.system("ifconfig wlan0 up")
    os.system("ifconfig eth0 up")
    print("\033[97mMac Adresini Orjinal Haline Geri Getirdim :).")
	
else:
    print("Sadece 1 yada 2 Tusuna Basmalisin :( Hadi Yeniden Dene Bakalim ","\a")
   







   

	
     
  
  
 

    

