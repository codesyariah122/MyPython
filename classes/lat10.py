class Kendaraan(object):

	def __init__(self, nama):
		self.nama = nama
		self.penumpang = []

	def tambah_penumpang(self, nama_penumpang):
		self.penumpang.append(nama_penumpang)

class Mobil(Kendaraan):
	def tambah_penumpang(self, nama_penumpang):
		if len(self.penumpang) < 4:
			super(Mobil, self).tambah_penumpang(nama_penumpang)


mobnas = Mobil('Cooper')

mobnas.tambah_penumpang("Isyana Sarasvati")
mobnas.tambah_penumpang("Raisa Andria")
mobnas.tambah_penumpang("Iim Marlina")

print("Penumpang : "+str(mobnas.penumpang))