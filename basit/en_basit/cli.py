#!/python
# -*- coding: utf-8 -*-

import socket as s

net = s.socket(s.AF_INET, s.SOCK_STREAM) 

HOST = "localhost"
PORT = 10040
net.connect((HOST,PORT))
net.settimeout(1.0)         # Bu satiri kaldýrýrsan, Client sürekli baðlý kalýr.
                            # 5 deðerini böyle býrakýrsan, baðlandýktan 5 saniye sonra düþer.
                            # Ýstersen 300 yap, 1000 yap. Keyfine kalmýþ :)
x = "Ahmet"            # Sunucuda kontrol edilecek olan kullanýcý adý. Yani Lis.txt'deki.
xx = "{}".format(x)
xxx = bytes(xx)
bufi=""
dat=""
data=""

while True:
    try:

        print "Lutfen isim yaziniz:"
        isim=raw_input()
        net.sendall(isim)
        print isim, " gonderildi..."

        data = net.recv()
        bufi+=data
        print "16 byte beklenmekte... "
        dat = bufi.decode("utf-8")   

        #net.shutdown(1) # By convention, but not actually necessary
        
        

    except s.error as socketerror:
        print("Error: ", socketerror)   
    
    finally:
        print(dat)
        net.close()     # Remember to close sockets after use! 
        
    if dat == "-":
       
       print "Bu ", isim, " listede yok! Tekrar dene..."

    elif dat=="+":  
        print "Tebrikler! ",isim,"..."     

       #break                 # - mesajý geldiyse; yani kayýtlý deðil ise baðlantýyý keser.                                 
