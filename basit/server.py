import socket
soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = "localhost"
PORT = 8000

soket.bind((HOST,PORT))
print "%s:%d server baþlatýldý." % (HOST,PORT)
print "Kullanýcý bekleniyor."
soket.listen(1)

baglanti,adres = soket.accept()
print "Bir baðlantý kabul edildi.", adres

baglanti.send("Hoþgeldiniz efendim , hoþgeldiniz.")

data = baglanti.recv(1024)
print data

soket.close()
