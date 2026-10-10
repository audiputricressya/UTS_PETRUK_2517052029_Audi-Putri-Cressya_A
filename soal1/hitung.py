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
