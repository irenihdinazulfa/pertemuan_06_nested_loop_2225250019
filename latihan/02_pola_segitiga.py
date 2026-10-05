# Input dari pengguna untuk menentukan tinggi segitiga
n = int(input("n: "))

# Loop luar: Mengatur nomor baris dari 1 sampai n
for i in range(1, n + 1):
    # Loop dalam: Mencetak bintang sebanyak nomor baris (i)
    for j in range(i):
        # Output: Mencetak karakter bintang tanpa pindah baris
        print("*", end=" ")
    # Output: Pindah ke baris baru setelah selesai mencetak bintang satu baris
    print()