# processing.py - class dan fungsi untuk mengolah & menganalisis data
from .validasi import validasi_teks, validasi_angka

BATAS_STOK_MENIPIS = 5       # konstanta (menghindari magic number)


def jumlahkan(*angka):
    """*args: menjumlahkan angka dalam jumlah tidak tentu (angka bertipe tuple)."""
    total = 0
    for a in angka:
        total += a
    return total


def hitung_rata_rata(*angka):
    """Rata-rata dari angka; assert memastikan ada minimal 1 data."""
    assert len(angka) > 0, "Tidak ada data untuk dihitung rata-ratanya"
    return jumlahkan(*angka) / len(angka)


class Barang:
    """Satu record barang di inventaris."""

    def __init__(self, kode, nama, harga, stok, kategori="Umum"):
        # validasi di sini; data tidak valid memunculkan DataTidakValidError
        self.kode = validasi_teks(kode, "kode")
        self.nama = validasi_teks(nama, "nama")
        self.harga = validasi_angka(harga, "harga", tipe=float)
        self.stok = validasi_angka(stok, "stok")
        self.kategori = validasi_teks(kategori, "kategori")

    def nilai_total(self):
        """Nilai stok = harga x stok."""
        return self.harga * self.stok

    def ke_baris(self):
        """Format satu baris untuk disimpan ke file."""
        return f"{self.kode};{self.nama};{self.harga:.0f};{self.stok};{self.kategori}"

    def __str__(self):
        return (f"{self.kode:<6} {self.nama:<18} Rp {self.harga:>10,.0f}  "
                f"stok {self.stok:>4}  [{self.kategori}]")


def buat_barang(kode, nama, harga, stok, **atribut):
    """**kwargs: atribut tambahan yang bervariasi (mis. kategori="Minuman")."""
    return Barang(kode, nama, harga, stok, kategori=atribut.get("kategori", "Umum"))


class Inventaris:
    """Kumpulan Barang beserta fungsi analisisnya."""

    def __init__(self):
        self.daftar = []

    def tambah(self, barang):
        self.daftar.append(barang)

    def cari(self, kode):
        """Mencari barang berdasarkan kode; None bila tidak ada."""
        for b in self.daftar:
            if b.kode == kode:
                return b
        return None

    def urutkan_harga(self, menurun=True):
        # lambda sebagai key pada sorted()
        return sorted(self.daftar, key=lambda b: b.harga, reverse=menurun)

    def stok_menipis(self, batas=BATAS_STOK_MENIPIS):
        # lambda pada filter()
        return list(filter(lambda b: b.stok <= batas, self.daftar))

    def total_nilai(self):
        return jumlahkan(*[b.nilai_total() for b in self.daftar])

    def rata_rata_harga(self):
        return hitung_rata_rata(*[b.harga for b in self.daftar])


def buat_laporan(inventaris, batas_stok=BATAS_STOK_MENIPIS):
    """Menyusun teks laporan analisis inventaris."""
    if not inventaris.daftar:
        return "Tidak ada data untuk dilaporkan.\n"
    termahal = inventaris.urutkan_harga()[0]
    baris = [
        "===== LAPORAN INVENTARIS TOKO =====",
        f"Jumlah jenis barang : {len(inventaris.daftar)}",
        f"Total nilai stok    : Rp {inventaris.total_nilai():,.0f}",
        f"Rata-rata harga     : Rp {inventaris.rata_rata_harga():,.0f}",
        f"Barang termahal     : {termahal.nama} (Rp {termahal.harga:,.0f})",
        f"Stok menipis (<= {batas_stok}):",
    ]
    menipis = inventaris.stok_menipis(batas=batas_stok)   # keyword argument
    if menipis:
        baris += [f"  - {b.nama} (stok {b.stok})" for b in menipis]
    else:
        baris.append("  (tidak ada)")
    return "\n".join(baris) + "\n"


# Pengujian lokal (jalankan: python -m inventaris.processing)
if __name__ == "__main__":
    inv = Inventaris()
    inv.tambah(buat_barang("B01", "Beras 5kg", 70000, 10, kategori="Sembako"))
    inv.tambah(buat_barang("B02", "Teh Botol", 5000, 3, kategori="Minuman"))
    print(buat_laporan(inv))
