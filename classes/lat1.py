class NamaKelas(object):

	properti_bersama = "Nilai Bersama"

	# fungsi inisialisasi

	def __init__(self, parameter_1, parameter_2):
		self.properti_pribadi_1 = parameter_1
		self.properti_pribadi_2 = parameter_2
		self.properti_pribadi_3 = ("Nilai", "Tupple", "Pribadi")

	def metode_lain(self):
		# lakuan sesuatu, contohnya
		print("Metode lain dipanggil")

objek = NamaKelas("Nilai string", True)

print(objek.properti_bersama)
print(objek.properti_pribadi_1)
print(objek.properti_pribadi_2)
print(objek.properti_pribadi_3)

objek.metode_lain()