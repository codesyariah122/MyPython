from lat1 import diskon

def kembali(total):
	bayar = int(total - diskon(total))
	print("Kembali : {0}".format(bayar))

print(kembali(400))