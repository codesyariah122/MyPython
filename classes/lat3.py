class Kendaraan(object):

	bahan_bakar = "bensin"
	nama = "Kendaraanku"

	def __init__(self, nama):
		self.nama = nama

mobil = Kendaraan("Mobil")
motor = Kendaraan("Motor")

print(mobil.nama)
print(motor.nama)