#!/usr/bin/python

import socket
import select

ADRES   = ''
PORT    = 10001
SUNUCU  = (ADRES, PORT)
TIMEOUT = 50

try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(SUNUCU)

        devam = True
        while devam:
                sock.listen(5)
                (cnn, adres) = sock.accept()

                while True:
                        (inp, out, exp) = select.select([cnn,], [], [], TIMEOUT)
                        if not inp: break

                        data = cnn.recv(1024)
                        if data == 'disconnect\r\n': break
                        if data == 'stop\r\n':
                                devam = False
                                break

                        print data.strip()

                cnn.close()
                print '---BAGLANTI KOPARTILDI-------------'
except: pass
finally:
        try: 
                sock.close()
                sys.exit()
                print "SOCKET KOPARTILDI!!!"

        except: pass
