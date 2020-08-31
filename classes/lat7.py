class Kendaraan(object):

	def __init__(self, nama):
		self.nama = nama
		self.penumpang = []

	def tambah_penumpang(self, nama_penumpang):
		self.penumpang.append(nama_penumpang)

# membuat class mobil yang merupakan turunan dari class kendaraan

class Mobil(Kendaraan):
	pintu_terbuka = False
	pintu_tertutup = False

	def buka_pintu(self):
		self.pintu_terbuka = True

	def tutup_pintu(self):
		self.pintu_tertutup = True

mobnas = Mobil("MobilSaya")

# mobnas akan memiliki properti dari kendaraan
mobnas.tambah_penumpang("Raisa")
print("Penumpang : "+str(mobnas.penumpang))

# dan memiliki properti mobil
mobnas.buka_pintu()
print("Pintu terbuka : "+str(mobnas.pintu_terbuka))

mobnas.tutup_pintu()
print("Pintu tertutup : "+str(mobnas.pintu_tertutup))
