# Counter untuk menghitung total pasangan
count = 0

# Loop luar: Mengatur nilai indeks i dari 1 sampai 3
for i in range(1, 4):
    # Loop dalam: Mengatur nilai indeks j dari 1 sampai 4
    for j in range(1, 5):
        # Output: Menampilkan pasangan indeks (i, j)
        print(i, j)
        # Counter: Menambahkan 1 ke total pasangan
        count += 1

# Output: Menampilkan total seluruh pasangan yang terbentuk
print(f"Banyak pasangan = {count}")