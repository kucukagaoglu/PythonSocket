# -*- coding: utf-8 -*-

import socket as s

net = s.socket(s.AF_INET, s.SOCK_STREAM)
sun = ('',10040)


net.bind(sun)                              # Host ve Port'u e�le�tirip..;
net.listen(0)                                # En fazla ba�lanacak ki�i say�s�. 0 olursa s�n�rs�z.

while True:                                  # Sunucunun s�rekli �al��mas� i�in.
    print('\nYeni baglanti bekleniyor..\n')
    kontak, ev = net.accept()              #..sunucuyu etkin hale getiriyoruz.
    
    try:
        with open("Lis.txt") as lis:         # *
            li = lis.read().splitlines()     # Sat�r sat�r okuma.
    
        print(ev,"baglandi.")
        
        data = kontak.recv(16)          # Sunucuya ba�lanmak isteyenin ismini de�i�kene at�yoruz.
        dat = data.decode("utf-8")
        
        if dat in li:                                       # E�er kay�tl� ise;   
            print(">>> {} su an oyunda.".format(dat))       # Eleman�n ismini yaz�p, ba�la..
            kontak.sendall("+")                            #..ve ona(Client'e) + mesaj� yolla.

        elif not dat in li:
            print(">>> {} kayitli degil!..".format(dat))
            kontak.sendall(b"-")
    
    except KeyboardInterrupt:
          net.close()
          print "baglanti kapatildi"

    finally:                            # Bu olmadan hata verir. �u manaya geliyor..;
      
        pass                           #..Minib�s bir durakta durup yolcu ald�ktan sonra..,
                                      #..yolcunun(Client) "devam et kaptan(Sunucu)" demesi gibi..
    
