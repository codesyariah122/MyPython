orang = {
	'nama': 'Linus Torvald',
	'tahun lahir': 1969,
	'warga negara': 'Finlandia'
}

for kunci in orang:
	print("{}: {}".format(kunci, orang[kunci]))


framework = {
	'nama': 'Django',
	'bahasa': 'Python',
	'tahun lahir': 2005,
	'versi': '1.9.6'
}
print("\n\n")
for f in framework:
	print("{}: {}".format(f, framework[f]))