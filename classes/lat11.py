class Kendaraan(object):
	km = 0

	def __init__(self, nama):
		self.nama = nama
		self.penumpang = []

	def tambah_penumpang(self, penumpang):
		self.penumpang.append(penumpang)

class Mobil(Kendaraan):	
	pintu_terbuka = False

	def buka_pintu(self):
		self.pintu_terbuka = True

	def tambah_penumpang(self, penumpang):
		if len(self.penumpang) < 4:
			super(Mobil, self).tambah_penumpang(penumpang)

mobilku = Mobil("Mobilku")
mobilku.buka_pintu()
mobilku.tambah_penumpang("Rosi")

print(mobilku.penumpang)
