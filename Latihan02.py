print("Program menampilkan bilangan terbesar dari n bilangan")
print ('')
print ("NAMA  : Ahmad Sobur")
print ("KELAS : TI.19.D.2")
print ("NIM   : 311910093")
print ('')

a = 1
max = 0
while a !=0:
    if a > max:
        max = a
    a = int(input("Masukkan bilangan:"))
    if a == 0:
        break
print("Nilai terbesar adalah:", max)
