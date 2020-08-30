for i in range(1000, 1, -200):
	print(i)

# sudah bisa juga untuk mencetak sebuah lists
for p in [2, 3, 5, 7, ]:
	print(p)

# termasuk mencetak string
for s in "string":
	print(s)

# dictionaty juga
dict = {
	'nama': 'saya',
	'umur': 22
}

for d in dict:
	# print(d+" : "+str(dict))
	print(d+" : {}".format(dict))