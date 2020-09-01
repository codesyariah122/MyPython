class Kendaraan(object):
	def __init__(self, nama):
		self.nama = nama
		self.penumpang = []

	def tambah_penumpang(self, nama_penumpang):
		self.penumpang.append(nama_penumpang)

class Motor(Kendaraan):
	standar_terpasang = False

	def pasang_standar(self):
		self.standar_terpasang = True

motorku = Motor("Motorku")
motorku.pasang_standar()
print("Motorku standar terpasang  : "+str(motorku.standar_terpasang))