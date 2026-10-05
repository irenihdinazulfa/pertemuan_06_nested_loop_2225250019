# Input dari pengguna untuk batas nilai n
n = int(input("n: "))

# Counter: Menghitung berapa pasangan (i, j) yang memenuhi kondisi
count = 0

# Loop luar: Mengatur nilai i dari 1 sampai n
for i in range(1, n + 1):
    # Loop dalam: Mengatur nilai j dari 1 sampai n
    for j in range(1, n + 1):
        # Kondisi: Memeriksa apakah jumlah i + j kurang dari atau sama dengan n
        if i + j <= n:
            # Counter: Menambahkan 1 ke total pasangan yang memenuhi kondisi
            count += 1

# Output: Menampilkan banyak pasangan yang memenuhi syarat
print(f"Banyak pasangan = {count}")