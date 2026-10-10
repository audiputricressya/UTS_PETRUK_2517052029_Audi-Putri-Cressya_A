import unittest
from suhu import analisis, hitung_rata_rata, kategori_suhu

class TestAnalisisSuhu(unittest.TestCase):
    def setUp(self):

        self.data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 33},
            {"hari": "Rabu", "suhu": 29},
            {"hari": "Kamis", "suhu": 35},
            {"hari": "Jumat", "suhu": 32},
            {"hari": "Sabtu", "suhu": 30},
            {"hari": "Minggu", "suhu": 28},
        ]

    def test_rata_rata(self):
        self.assertAlmostEqual(hitung_rata_rata(31, 33, 29, 35, 32, 30, 28), 31.142857, places=5)

    def test_tertinggi_dan_terendah(self):
        hasil = analisis(self.data)
        self.assertEqual(hasil["tertinggi"]["hari"], "Kamis")
        self.assertEqual(hasil["terendah"]["hari"], "Minggu")

    def test_kategori_batas(self):
        self.assertEqual(kategori_suhu(32), "Panas")    # tepat di batas = Panas
        self.assertEqual(kategori_suhu(31), "Normal")

    def test_jumlah_hari_panas(self):
        self.assertEqual(analisis(self.data)["jumlah_panas"], 3)
if __name__ == "__main__":
    unittest.main()
