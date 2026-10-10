# fileio.py - baca / tulis / tambah file (semua memakai with open)
from .processing import Inventaris, buat_barang
from .validasi import DataTidakValidError, validasi_baris


def buat_file_data(nama_file):
    """Mode 'x': membuat file data pertama kali, tidak menimpa file yang sudah ada."""
    try:
        with open(nama_file, "x"):
            pass
        print(f"File {nama_file} berhasil dibuat.")
    except FileExistsError:
        print(f"Gagal: file {nama_file} sudah ada, tidak ditimpa.")


def tambah_barang_ke_file(nama_file, barang):
    """Mode 'a': menambah data baru di akhir file tanpa menghapus data lama."""
    with open(nama_file, "a") as file:
        file.write(barang.ke_baris() + "\n")
    print("Data barang berhasil disimpan.")


def baca_inventaris(nama_file):
    """Mode 'r' secara iteratif. Baris rusak dilewati, bukan menghentikan program."""
    inventaris = Inventaris()
    try:
        with open(nama_file, "r") as file:
            for nomor, baris in enumerate(file, start=1):   # baca baris demi baris
                if baris.strip() == "":
                    continue
                try:
                    kode, nama, harga, stok, kategori = validasi_baris(baris)
                    inventaris.tambah(buat_barang(kode, nama, harga, stok, kategori=kategori))
                except DataTidakValidError as e:
                    print(f"[Peringatan] Baris {nomor} dilewati: {e}")
    except FileNotFoundError:
        print(f"Error: file {nama_file} belum ada. Buat file terlebih dahulu (menu 1).")
    return inventaris


def tulis_laporan(nama_file, isi):
    """Mode 'w': menulis (menimpa) file laporan dengan hasil terbaru."""
    with open(nama_file, "w") as file:
        file.write(isi)


def tampilkan_file(nama_file):
    """Mode 'r': membaca seluruh isi file untuk ditampilkan."""
    with open(nama_file, "r") as file:
        print(file.read())


# Pengujian lokal (jalankan: python -m inventaris.fileio)
if __name__ == "__main__":
    baca_inventaris("file_yang_tidak_ada.txt")
