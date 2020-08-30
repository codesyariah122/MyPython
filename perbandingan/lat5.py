uang = 6000
harga = 1500

print("A: Harga kudanya berapa ya ?")
print("B: "+str(harga))

if uang >= harga*4:
	print("A: kita beli 4 ekor")
elif uang == harga*2:
	print("A: Kita beli 2 ekor")
	print("B: Mantap pak ! ")
else:
	print("A: Bisa dikurangi ? ")
	print("B: Belum bisa mas, segitu udah pasnya!")
	print("A: Ok bailah !")
