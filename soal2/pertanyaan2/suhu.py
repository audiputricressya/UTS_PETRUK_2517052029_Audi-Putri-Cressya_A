# suhu.py - analisis suhu harian stasiun cuaca

# # ---------- Tahap 1: Baca data ----------
def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r") as file:           
            for baris in file:
                if baris.strip() == "":              
                    continue
                hari, suhu = baris.strip().split(";")
                data.append({"hari": hari, "suhu": float(suhu)})
    except FileNotFoundError:
        print(f"Error: file {nama_file} tidak ditemukan.")
    return data

# # ---------- Tahap 2: Analisis ----------
def hitung_rata_rata(*suhu):
    return sum(suhu) / len(suhu)


kategori_suhu = lambda suhu, batas=32: "Panas" if suhu >= batas else "Normal"


def analisis(data, batas_panas=32):
    rata = hitung_rata_rata(*[d["suhu"] for d in data])
    tertinggi = max(data, key=lambda d: d["suhu"])   
    terendah = min(data, key=lambda d: d["suhu"])
    for d in data:
        d["kategori"] = kategori_suhu(d["suhu"], batas=batas_panas)  
    jumlah_panas = len([d for d in data if d["kategori"] == "Panas"])
    return {
        "rata_rata": rata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "jumlah_panas": jumlah_panas,
        "data": data,
    }

data_suhu = baca_data("suhu.txt")
hasil = analisis(data_suhu)


# # ---------- Tahap 3: Tulis laporan ----------
def tulis_laporan(nama_file, hasil):
    with open(nama_file, "w") as file:
        file.write("===== LAPORAN SUHU MINGGUAN =====\n")
        for d in hasil["data"]:
            file.write(f"{d['hari']:<7}: {d['suhu']} C ({d['kategori']})\n")
        file.write(f"Rata-rata suhu   : {hasil['rata_rata']:.2f} C\n")
        file.write(f"Suhu tertinggi   : {hasil['tertinggi']['suhu']} C ({hasil['tertinggi']['hari']})\n")
        file.write(f"Suhu terendah    : {hasil['terendah']['suhu']} C ({hasil['terendah']['hari']})\n")
        file.write(f"Jumlah hari Panas: {hasil['jumlah_panas']} hari\n")


def tampilkan_laporan(nama_file):
    with open(nama_file, "r") as file:
        print(file.read())


def main():
    data = baca_data("suhu.txt")
    if not data:                                     
        return
    hasil = analisis(data, batas_panas=32)
    tulis_laporan("laporan_suhu.txt", hasil)
    tampilkan_laporan("laporan_suhu.txt")


if __name__ == "__main__":
    main()
