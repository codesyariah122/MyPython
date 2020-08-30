mobil_1 = { "warna" : "merah", "jumlah pintu": 4 }
mobil_2 = { "warna" : "putih", "jumlah pintu": 2 }

daftar_mobil = []

coder = { 'nama' : 'anda',
  'jomblo' : True }

# tambahkan mobil_1 dan mobil_2 ke daftar_mobil
# masih ingat cara menambahkan ke list? (hint: append)
daftar_mobil = [mobil_1, mobil_2]
daftar_mobil.append(daftar_mobil)
# berikan kunci baru bernama 'mobil' ke coder
# dan berikan nilai daftar_mobil
coder['mobil'] = daftar_mobil


# hapus 'jomblo' di coder
# kita mau tidak ada yang tahu XD
del coder['jomblo']

# kita lihat seperti apa coder sekarang
print(coder)