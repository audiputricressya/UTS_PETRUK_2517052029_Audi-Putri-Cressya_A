# Tabel Refactoring

| No | Bagian yang belum diperbaiki | Bagian yang diperbaiki | Teknik refactoring | Alasan |
|----|------------------------------|------------------------|--------------------|--------|
| 1 | `h = input(...)`, `s = input(...)`, `k = ...` | `harga`, `stok`, `kategori` | Rename Variable | Nama deskriptif sehingga maksud variabel langsung terbaca |
| 2 | Pengecekan angka/negatif/kosong ditulis berulang di setiap tempat input | Fungsi `validasi_teks()` dan `validasi_angka()` di `validasi.py` | Remove Duplicate Code | Aturan validasi cukup diubah di satu tempat |
| 3 | Satu fungsi `main()` panjang berisi seluruh logika menu (input, simpan, baca, laporan) | `menu_buat_file()`, `menu_tambah_barang()`, `menu_tampilkan()`, `menu_laporan()`, `menu_uji()` | Extract Function | Fungsi pendek, satu tugas, mudah diuji & dipakai ulang |
| 4 | Angka `5` ditulis langsung pada pengecekan stok | Konstanta `BATAS_STOK_MENIPIS = 5` | Replace Magic Number with Constant | Makna angka jelas dan mudah diubah |
| 5 | Semua kode dalam satu file | Package `inventaris` (fileio, processing, validasi, testing) | Extract Module | Pembagian tugas jelas, kode mudah dipelihara |
