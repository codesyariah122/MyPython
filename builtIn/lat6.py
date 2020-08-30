def diskon(harga):
	if harga > 300:
		return float(harga)/10
	elif harga > 100:
		return float(harga)/20
	else:
		return 0

print(diskon(400))
print(diskon(200))