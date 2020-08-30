# minuman = ["kopi", "teh", "susu", "bandrek"]

# for drink in minuman:
# 	print("Saya minum {}".format(drink))

kelas = [ "Python", "PHP", "JS"]

# mengakses indeks
print(kelas[0])

# mengupdate suatu item
kelas[2] = "JavaScript"

# menambahkan item
kelas.append("Git")

# mengiris item
server_side = kelas[:2]

# memeriksa item di list
print("Python" in kelas)

# dan menggunakan for
for k in kelas:
  print(k)