from random import randint

hitung_kepala = 0
hitung_total = 0

while True:
  
  # angka integer acak: 0 atau 1
  putar  = randint(0,1)
  
  if putar:
    hitung_kepala  = hitung_kepala + 1
    print(str(hitung_total) + " kepala " + str(hitung_kepala))
  else:
    hitung_kepala = 0
    print(str(hitung_total) + " buntut")
    
  hitung_total = hitung_total + 1

  if not (hitung_kepala < 3 and hitung_total < 100):
    break

print("Muncul kepala " + str(hitung_kepala) + " kali berturut-turut.")