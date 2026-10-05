# Loop luar: Mengatur nilai indeks i dari 1 sampai 4
for i in range(1, 5):
    # Akumulator: Menyimpan total hasil kali i * j untuk baris ke-i (di-reset di setiap baris)
    total_baris = 0
    # Loop dalam: Mengatur nilai indeks j dari 1 sampai 3
    for j in range(1, 4):
        # Akumulator: Menjumlahkan hasil perkalian i * j
        total_baris += i * j
    # Output: Menampilkan hasil jumlah perkalian untuk baris ke-i
    print(f"Jumlah baris {i} = {total_baris}")