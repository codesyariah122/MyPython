def diskon(harga):
  if harga > 300:
    return harga / 10
  elif harga >= 100:
    return harga / 20
  else:
    return 0
  
print (diskon(500))