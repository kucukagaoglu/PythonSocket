#!/usr/bin/python
# -*- encoding: utf-8 -*-
#ax-udp-sunucu.py
from socket import *
sunucuAd = 'localhost'
sunucuPort = 12349
sunucuSocket = socket(AF_INET, SOCK_DGRAM)
sunucuSocket.bind((sunucuAd,sunucuPort))
print ('Sunucu veri almaya hazırdır')
while 1:
    mesaj, istemciAdres = sunucuSocket.recvfrom(4096)
    if mesaj == 'axson':
        break
    yeniMesaj = mesaj.upper()
    print "Gelen=",mesaj, ", gonderilen= ",yeniMesaj
    sunucuSocket.sendto(yeniMesaj,istemciAdres)
sunucuSocket.close()
print ('Sunucu kapandı.')
