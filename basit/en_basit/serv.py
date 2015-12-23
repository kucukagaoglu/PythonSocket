# -*- coding: utf-8 -*-

import socket as s

net = s.socket(s.AF_INET, s.SOCK_STREAM)
sun = ('',10040)


net.bind(sun)                              # Host ve Port'u eþleþtirip..;
net.listen(0)                                # En fazla baðlanacak kiþi sayýsý. 0 olursa sýnýrsýz.

while True:                                  # Sunucunun sürekli çalýþmasý için.
    print('\nYeni baglanti bekleniyor..\n')
    kontak, ev = net.accept()              #..sunucuyu etkin hale getiriyoruz.
    
    try:
        with open("Lis.txt") as lis:         # *
            li = lis.read().splitlines()     # Satýr satýr okuma.
    
        print(ev,"baglandi.")
        
        data = kontak.recv(16)          # Sunucuya baðlanmak isteyenin ismini deðiþkene atýyoruz.
        dat = data.decode("utf-8")
        
        if dat in li:                                       # Eðer kayýtlý ise;   
            print(">>> {} su an oyunda.".format(dat))       # Elemanýn ismini yazýp, baðla..
            kontak.sendall("+")                            #..ve ona(Client'e) + mesajý yolla.

        elif not dat in li:
            print(">>> {} kayitli degil!..".format(dat))
            kontak.sendall(b"-")
    
    except KeyboardInterrupt:
          net.close()
          print "baglanti kapatildi"

    finally:                            # Bu olmadan hata verir. Þu manaya geliyor..;
      
        pass                           #..Minibüs bir durakta durup yolcu aldýktan sonra..,
                                      #..yolcunun(Client) "devam et kaptan(Sunucu)" demesi gibi..
    
