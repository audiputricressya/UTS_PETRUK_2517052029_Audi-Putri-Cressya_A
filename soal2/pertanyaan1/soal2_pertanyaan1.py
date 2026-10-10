#ini nomor 3 (perbaikan)
def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r") as file:               
            for baris in file:                           
                try:
                    npm, nama, nilai = baris.strip().split(";")
                    data.append({"npm": npm, "nama": nama, "nilai": int(nilai)})
                except ValueError:                       
                    continue                             
    except FileNotFoundError:
        print(f"Error: file {nama_file} belum ada")
    return data


# nomor 5 (dampak dan solusi)
def buat_file(nama_file):
    try:
        with open(nama_file, "x") as file:
            file.write("")
        print(f"File {nama_file} berhasil dibuat.")
    except FileExistsError:
        print(f"Gagal: file {nama_file} sudah ada, tidak ditimpa.")


def tambah_data(nama_file, npm, nama, nilai):
    with open(nama_file, "a") as file:
        file.write(f"{npm};{nama};{nilai}\n")


#program utamanya
if __name__ == "__main__":
    hasil = baca_data("nilai.txt")
    print(hasil)                      # baris Budi (abc) dilewati

    print("\n--- Uji file tidak ada ---")
    baca_data("tidak_ada.txt")        # pesan error FileNotFoundError

    print("\n--- Uji mode x pada file yang sudah ada ---")
    buat_file("nilai.txt")            # FileExistsError ditangani
