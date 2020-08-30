laptop = {
	'warna': 'perak',
	'processor': 'i7',
	'merk': 'apple',
	'layar': '4k'
}

if 'harga' in laptop:
	print(laptop['harga'])
else:
	print("Harga belum terdaftar")

laptop['harga'] = 7000000

print("Harga laptop : {}".format(laptop['harga']))