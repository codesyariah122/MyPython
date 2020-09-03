# def diskon(harga):
#   if harga > 300:
#     return harga / 10
#   elif harga >= 100:
#     return harga / 20
#   else:
#     return 0
  
# print (diskon(500))

angka = [100, 200, 300, 400]

# angkabaru = int(input("Tambahkan Angka baru : ? "))
# while(angkabaru == 0):
# 	print("please tambahkan angka baru ! ")
# 	angkabaru = int(input("Tambahkan angka baru : ? "))

# if angkabaru:
# 	angka.append(angkabaru)

# 	for x in range(len(angka)):
# 		var = str(angka[x])

# 		print("Angka : "+var)

# while True:
# 	try:
# 		angkabaru = int(input("Angka baru : ? "))
# 	except ValueError:
# 		break

# 	if angkabaru:
# 		angka.append(angkabaru)
# 		for x in angka:
# 			# range(len(angka))
# 			# var = str(angka[x])
# 			print(x)

add_makanan = []
while True:
	user_input = input("Daftarkan makanan kesukaan anda : ? ")
	if user_input != "":
		add_makanan.append(user_input)
	else:
		break

print(add_makanan)