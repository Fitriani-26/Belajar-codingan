PEMBAHASAN PERTAMA (TIPE DATA DAN VARIABEL PYTHON)
# integer = bilangan bulat
print (20)

# float = bilangan desimal atau pecahan
print (1.75)

# string = teks 
print ("hello friends")

# boolean = True dan False
2 > 8
2 < 5

# Variabel 

tinggi = 200
type (tinggi)

luas = 1.90
type(luas)

nama = "dani"
type(nama)

mahasiswa = True
type (mahasiswa)

PEMBAHASAN KEDUA (OPERATOR)

OPERATOR ARITMATIKA
OPERATOR PENUGASAN
OPERATOR PERBANDINGAN
OPERATOR LOGIKA

Operator aritmatika
angka1 = 10
angka2 = 3

# penjumlahan (+)
hasil = angka1 + angka2
print(hasil)

# pengurangan (-)
hasil = angka1 - angka2
print(hasil)

# perkalian (*)
hasil = angka1 * angka2
print(hasil)

# perpangkatan (**)
hasil = angka1 ** angka2
print(hasil)

# pembagian (/)
hasil = angka1 / angka2
print(hasil)

# pembagian bilangan bulat (//)
hasil = angka1 // angka2
print(hasil)

# sisa bagi (%)
hasil = angka1 % angka2
print(hasil)

Operator penugasan
nilai = 5

# penjumlahan
nilai += 3 # nilai = nilai + 3
print(nilai)

# pengurangan 
nilai -= 3 # nilai = nilai - 3
print(nilai)

# perkalian
nilai *= 3 # nilai = nilai * 3
print(nilai)

# pembagian
nilai /= 3 # nilai = nilai / 3
print(nilai)

# pembagian bilangan bulat 
nilai //= 3 # nilai = nilai // 3
print(nilai)

# perpangkatan 
nilai **= 3 # nilai = nilai ** 3
print(nilai)

# sisa bagi
nilai %= 3 # nilai = nilai % 3
print(nilai)

Operator perbandingan
a = 8
b = 6

# lebih dari 
print(a > b)

# kurang dari 
print (a < b)

# setara / sama dengan 
print(a == b)

# tidak setara / tidak sama dengan
print(a != b)

# lebih dari atau sama dengan
print(a >= b)

# kurang dari atau sama dengan
print(a <= b)

Operator logika
# operator and
x = False
y = True
print(x and y)

# operator or 
x = True
y = False
print(x or y)

# operator not
x = False
print(not x)
y = True
print (not y)

PEMBAHASAN KETIGA (PERCABANGAN )
# Kondisi if 
# kondisi if bernilai salah
nilai = 10
if nilai > 20 :
  print ("cetak ini jika benar")

# kondisi if bernilai benar
nilai = 21
if nilai > 20 :
  print ("cetak ini jika benar")
  
  # kondisi if-else
# kondisi if bernilai salah
nilai = 10
if nilai > 20 :
  print ("cetak ini jika benar")
else :
  print ("cetak ini jika salah")

# kondisi if bernilai benar
nilai = 21
if nilai > 20 :
  print ("cetak ini jika benar")
else :
  print ("cetak ini jika salah")

# kondisi if-elif-else
# kondisi if bernilai benar
nilai = 10
if nilai > 7 :
  print ("cetak ini jika benar")
elif nilai % 2 == 0:
  print ("cetak ini jika kondisi elif dijalankan ")
else :
  print ("cetak ini jika salah")

# kondisi if bernilai salah dan kondis elif benar
nilai = 6
if nilai > 7 :
  print ("cetak ini jika benar")
elif nilai % 2 == 0:
  print ("cetak ini jika kondisi elif dijalankan ")
else :
  print ("cetak ini jika salah")

# kondisi if bernilai salah dan kondis elif salah 
nilai = 5
if nilai > 5 :
  print ("cetak ini jika benar")
elif nilai % 2 == 0:
  print ("cetak ini jika kondisi elif dijalankan ")
else :
  print ("cetak ini jika salah")

