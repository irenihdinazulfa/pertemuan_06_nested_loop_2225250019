print("Tabel Perkalian dan Statistik")

# 1. Validasi input n dengan while (harus n > 0)
n = int(input("n: "))
while n <= 0:
    print("Nilai n harus berupa bilangan bulat positif!")
    n = int(input("n: "))

# 2. Inisialisasi variabel akumulator & counter
total_semua = 0
count_genap = 0

# 3. Nested loop untuk membuat tabel perkalian dan statistik
for i in range(1, n + 1):
    total_baris = 0
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil}\t", end="")
        
        # Hitung akumulasi
        total_baris += hasil
        
        # Cek apakah hasil perkalian genap
        if hasil % 2 == 0:
            count_genap += 1
            
    print(f"| Jumlah baris {i} = {total_baris}")
    total_semua += total_baris

# 4. Tampilkan total keseluruhan dan banyak hasil genap
print("-" * 35)
print(f"Total semua = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")