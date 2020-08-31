class Gadget(object):
	pembuat = [] # variable bersama
	
	def __init__(self):
		self.fitur = [] # variable pribadi

	def tambah_fitur(self, fitur):
		self.fitur.append(fitur)

	def tambah_pembuat(self, pembuat):
		self.pembuat.append(pembuat)

hp = Gadget()
tablet = Gadget()

hp.tambah_pembuat("Apple")
tablet.tambah_pembuat("Samsung")

hp.tambah_fitur("Telepon")
hp.tambah_fitur("Video Call")

tablet.tambah_fitur("Layar")

print("Fitur HP : "+str(hp.fitur))
print("Fitur Tablet : "+str(tablet.fitur))