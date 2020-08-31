class Kendaraan(object):
	km = 100

	def __init__(self, nama):
		self.nama = nama

	def jalan(self, jarak):
		self.km+jarak

mobil = Kendaraan("Mobil")

print(mobil.km)
mobil.jalan(100)