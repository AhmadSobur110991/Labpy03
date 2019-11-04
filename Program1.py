print ("Program Perulangan nilai Investasi")
print ('')
print ("NAMA  : Ahmad Sobur")
print ("KELAS : TI.19.D.2")
print ("NIM   : 311910093")
print ('')
x=100000000
sum=0
y=0
laba = [int(0), int(0), int(x) * .1, int (x) * .1, int(x) * .5, int(x) * .5, int(x) * .5, int(x) * .2]
print("Investasi awal seorang pengusaha:", x)
for i in laba :
    sum = sum+i
    y+=1
    print("Laba bulan ke-",y,"sebesar:", i)
print("Total laba adalah:", sum)
