#mac adresi değiştirme

import os

mac = input("Mac adresi değiştirilsinmi ?:")

a=1
while a < 2:
    print("Mac adresi değiştiriliyor...")
    a=a+1
    os.system("ifconfig wlan1 down")
    os.system("macchanger -r wlan1")
    os.system("service networking restart")
    os.system("service network-manager restart")

b=1
while b < 2:
    print("Mac adresi değiştiriliyor...")
    b=b+1
    os.system("ifconfig wlan1 down")
    os.system("macchanger -r wlan1")
    os.system("service networking restart")
    os.system("service network-manager restart")

c=1
while c < 2:
    print("Mac adresi değiştiriliyor...")
    c=c+1
    os.system("ifconfig wlan1 down")
    os.system("macchanger -r wlan1")
    os.system("service networking restart")
    os.system("service network-manager restart")


print("Mac adresi değiştirildi !")


