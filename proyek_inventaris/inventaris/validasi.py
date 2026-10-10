# validasi.py - pengecekan input dan data

class DataTidakValidError(Exception):
    """Exception buatan sendiri untuk data barang yang tidak valid."""


def validasi_teks(nilai, nama_field):
    """Memastikan field teks tidak kosong."""
    if nilai is None or str(nilai).strip() == "":
        raise DataTidakValidError(f"Field '{nama_field}' tidak boleh kosong")  # raise
    return str(nilai).strip()


def validasi_angka(nilai, nama_field, tipe=int):
    """Mengonversi ke angka dan memastikan tidak negatif."""
    try:
        angka = tipe(nilai)
    except (ValueError, TypeError):                 # konversi gagal (mis. "abc")
        raise DataTidakValidError(f"Field '{nama_field}' harus angka, bukan '{nilai}'")
    if angka < 0:
        raise DataTidakValidError(f"Field '{nama_field}' tidak boleh negatif")  # raise
    return angka


def validasi_baris(baris):
    """Memecah satu baris file (kode;nama;harga;stok;kategori) dan cek jumlah kolom."""
    bagian = baris.strip().split(";")
    if len(bagian) != 5:
        raise DataTidakValidError(f"Jumlah kolom harus 5, ditemukan {len(bagian)}")
    return bagian


if __name__ == "__main__":
    print(validasi_angka("15000", "harga", tipe=float))
    try:
        validasi_angka("abc", "stok")
    except DataTidakValidError as e:
        print("Error tertangkap:", e)
