nilai_budi = ["80", "75", "90"]
total = 0
for n in nilai_budi:
    total = total + n
    rata = total / len(nilai_budi)

print("Nama : Budi")
print("Rata-rata :", rata)

if rata >= 70:
    print("Status : Lulus")
else:
    print("Status : Tidak Lulus")
    
nilai_sari = ["60", "65", "55", "70"]
total = 0
for n in nilai_sari:
    total = total + n
rata = total / len(nilai_sari)

print("Nama : Sari")
print("Rata-rata :", rata)

if rata >= 70:
    print("Status : Lulus")
else:
    print("Status : Tidak Lulus")

def hitung_rata_rata(*nilai):
    return sum(nilai) / len(nilai)

tentukan_status = lambda rata, batas=70: "Lulus" if rata >= batas else "Tidak Lulus"


def tampilkan_hasil(nama, *nilai, batas=70):
    rata = hitung_rata_rata(*nilai)
    print("Nama :", nama)
    print("Rata-rata :", rata)
    print("Status :", tentukan_status(rata, batas=batas))

if __name__ == "__main__":
    print("=== Pengujian lokal hitung.py ===")
    tampilkan_hasil("Uji", 70, 80, 90)
