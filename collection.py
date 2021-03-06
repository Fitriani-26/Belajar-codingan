# -*- coding: utf-8 -*-
"""Collection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D06OGxMIr0YVqUzBClm4Lh1h7UGQ3WC9

Collection 
1. List
2. Tuple
3. Dictionary
4. Set
"""

# list
hewan = ['ayam', 'anjing', 'burung']
for i in hewan:
  print (i)

# mengupdate 
hewan[1] = 'kucing'
print (hewan)

# menambahkan
# append
hewan.append ('serigala')
print (hewan)

# extend 
hewan.extend (['ular', 'cacing'])
print (hewan)

# insert
hewan.insert (0, 'harimau')
print (hewan)

# menghapus
# del
del hewan[0]
print (hewan)

# remove 
hewan.remove ('cacing')
print (hewan)

# pop 
hewan.pop ()
print (hewan)

# tuple
mytuple = ("kursi", "meja", "bantal", "buku")
for i in mytuple:
  print (i)

# mengupdate 
mylist = list(mytuple)
mylist[0] = "handphone"
mytuple = tuple(mylist)
print (mytuple)

# menambahkan
# append
mylist = list(mytuple)
mylist.append ("sendok")
mytuple = tuple(mylist)
print (mytuple)

# menghapus 
# pop
mylist = list(mytuple)
mylist.pop()
mytuple = tuple(mylist)
print (mytuple)

# dictionary 
myidentitas = {"nama":"nabila", "umur":"19", "jurusan":"teknik"}
for i in myidentitas.items():
  print(i)

# mengupdate
myidentitas['nama'] = 'fitriani'
print (myidentitas)

# menambahkan
myidentitas ['status'] = 'mahasiswa'
print (myidentitas)

# menghapus 
myidentitas.pop ('status')
print (myidentitas)

# set 
myset = {"anggur", "pisang", "mangga", "apel"}
for i in myset:
  print (i)

# mengupdate
myset = list (myset)
myset [0] = "delima"
print (myset)

# menambahkan
# add
myset = set (myset)
myset.add ("kiwi")
print(myset)

# menghapus
# discard
myset.discard ('pisang')
print (myset)

# clear 
myset.clear()
print (myset)