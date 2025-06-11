def konversi_desimal(desimal):
  biner = bin(desimal)[2:]
  oktal = oct(desimal)[2:]
  heksadesimal = hex(desimal)[2:]

  hasil = {
      "biner": biner,
      "oktal": oktal,
      "heksadesimal": heksadesimal
  }
  return hasil

desimal = 95

hasil_konversi = konversi_desimal(desimal)

print(f"Bilangan Desimal: {desimal}")
print(f"Biner: {hasil_konversi['biner']}")
print(f"Oktal: {hasil_konversi['oktal']}")
print(f"Heksadesimal: {hasil_konversi['heksadesimal']}")
