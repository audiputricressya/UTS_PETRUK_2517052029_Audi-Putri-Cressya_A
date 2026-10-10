# testing.py - pengujian program menggunakan library unittest
import os
import tempfile
import unittest

from .validasi import DataTidakValidError, validasi_angka, validasi_teks
from .processing import Inventaris, buat_barang, hitung_rata_rata, jumlahkan
from .fileio import baca_inventaris


class TestInventaris(unittest.TestCase):
    def setUp(self):
        # test fixture: inventaris contoh + folder sementara
        self.inv = Inventaris()
        self.inv.tambah(buat_barang("B01", "Beras", 70000, 10, kategori="Sembako"))
        self.inv.tambah(buat_barang("B02", "Teh", 5000, 3, kategori="Minuman"))
        self.folder = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.folder.cleanup()

    def test_nilai_total_barang(self):
        self.assertEqual(self.inv.cari("B01").nilai_total(), 700000)

    def test_jumlahkan_args(self):
        self.assertEqual(jumlahkan(1, 2, 3, 4), 10)

    def test_rata_rata_kosong_memicu_assert(self):
        with self.assertRaises(AssertionError):
            hitung_rata_rata()

    def test_harga_negatif_memicu_exception(self):
        with self.assertRaises(DataTidakValidError):
            buat_barang("B03", "Gula", -100, 5)

    def test_field_kosong_memicu_exception(self):
        with self.assertRaises(DataTidakValidError):
            validasi_teks("   ", "nama")

    def test_stok_bukan_angka(self):
        with self.assertRaises(DataTidakValidError):
            validasi_angka("abc", "stok")

    def test_urut_harga_menurun(self):
        self.assertEqual(self.inv.urutkan_harga()[0].kode, "B01")

    def test_stok_menipis(self):
        hasil = self.inv.stok_menipis(batas=5)
        self.assertEqual([b.kode for b in hasil], ["B02"])

    def test_baca_file_lewati_baris_rusak(self):
        path = os.path.join(self.folder.name, "data.txt")
        with open(path, "w") as f:
            f.write("B01;Beras;70000;10;Sembako\nB02;Teh;abc;3;Minuman\nB03;Gula;12000;7;Sembako\n")
        hasil = baca_inventaris(path)
        self.assertEqual(len(hasil.daftar), 2)     # baris rusak dilewati

    def test_file_tidak_ada(self):
        hasil = baca_inventaris(os.path.join(self.folder.name, "tidak_ada.txt"))
        self.assertEqual(hasil.daftar, [])


if __name__ == "__main__":
    unittest.main()
