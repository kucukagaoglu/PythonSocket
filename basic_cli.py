#!/usr/bin/python
# -*- encoding: utf-8 -*-
#ax-udp-istemci.py
from socket import *
sunucuAd = 'localhost'
sunucuPort = 12349
istemciSocket = socket(AF_INET, SOCK_DGRAM) #datagram
while 1:
    mesaj = raw_input('Küçük harfle bir cümle yaz:')
    istemciSocket.sendto(mesaj, (sunucuAd, sunucuPort))
    yeniMesaj, sunucuAdres = istemciSocket.recvfrom(4096)
    print (yeniMesaj)
    mesaj=""
istemciSocket.close()
