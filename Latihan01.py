print ("Program untuk bilangan acak yang lebih kecil dari 0.5 ")
print ('')
print ("NAMA  : Ahmad Sobur")
print ("KELAS : TI.19.D.2")
print ("NIM   : 311910093")
print ('')
import random
n=int(input("Masukkan Nilai Bilangan N :"))

jumlah = n
for i in range(jumlah):
    while 1:
        n = random.random()
        if n < 0.5 :
            break
    print (n)
print ("Selesai")
