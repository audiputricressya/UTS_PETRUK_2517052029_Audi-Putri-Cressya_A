import unittest

import inventaris as inv
from inventaris import testing

NAMA_FILE_DATA = "data_inventaris.txt"
NAMA_FILE_LAPORAN = "laporan_inventaris.txt"


def menu_buat_file():
    inv.buat_file_data(NAMA_FILE_DATA)


def menu_tambah_barang():
    kode = input("Kode barang : ")
    nama = input("Nama barang : ")
    harga = input("Harga       : ")
    stok = input("Stok        : ")
    kategori = input("Kategori    : ") or "Umum"
    try:
        barang = inv.buat_barang(kode, nama, harga, stok, kategori=kategori)
    except inv.DataTidakValidError as e:
        print("Input tidak valid:", e)
        return
    inv.tambah_barang_ke_file(NAMA_FILE_DATA, barang)


def menu_tampilkan():
    inventaris = inv.baca_inventaris(NAMA_FILE_DATA)
    if not inventaris.daftar:
        print("Belum ada data barang yang dapat ditampilkan.")
        return
    for barang in inventaris.daftar:
        print(barang)


def menu_laporan():
    inventaris = inv.baca_inventaris(NAMA_FILE_DATA)
    isi = inv.buat_laporan(inventaris, batas_stok=inv.BATAS_STOK_MENIPIS)
    inv.tulis_laporan(NAMA_FILE_LAPORAN, isi)
    inv.tampilkan_file(NAMA_FILE_LAPORAN)


def menu_uji():
    suite = unittest.defaultTestLoader.loadTestsFromModule(testing)
    unittest.TextTestRunner(verbosity=2).run(suite)


def main():
    menu = {"1": menu_buat_file, "2": menu_tambah_barang, "3": menu_tampilkan,
            "4": menu_laporan, "5": menu_uji}
    while True:
        print("\n=== INVENTARIS TOKO ===")
        print("1. Buat file data\n2. Tambah barang\n3. Tampilkan semua barang")
        print("4. Laporan analisis\n5. Jalankan pengujian\n0. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "0":
            print("Program selesai.")
            break
        aksi = menu.get(pilihan)
        if aksi:
            aksi()
        else:
            print("Menu tidak tersedia.")


if __name__ == "__main__":
    main()
