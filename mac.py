#mac adresi değiştirme

import os

mac = input("Mac adresi değiştirilsinmi ?:")

a=1
while a < 2:
    print("Mac adresi değiştiriliyor...")
    a=a+1
    os.system("ifconfig wlan0 down")
    os.system("macchanger -r wlan0")
    os.system("service networking restart")
    os.system("service network-manager restart")

print("Mac adresi değiştirildi !")


