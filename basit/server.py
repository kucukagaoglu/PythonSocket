import socket
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = "localhost"
PORT = 8000

soket.bind((HOST,PORT))
print "%s:%d server ba�lat�ld�." % (HOST,PORT)
print "Kullan�c� bekleniyor."
soket.listen(1)

baglanti,adres = soket.accept()
print "Bir ba�lant� kabul edildi.", adres

baglanti.send("Ho�geldiniz efendim , ho�geldiniz.")

data = baglanti.recv(1024)
print data

soket.close()
