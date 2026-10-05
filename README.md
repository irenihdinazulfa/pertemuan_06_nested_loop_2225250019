Nama: Iren Ihdina Zulfa
NIM: 2225250019
Kelas: 3E

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan untuk menyelesaikan masalah perhitungan matematika dan statistik.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
- **Loop Luar**: Bertanggung jawab untuk mengontrol nomor baris ($i$) dari $1$ sampai $n$, mencetak pemisah antar-baris, serta mengatur reset nilai `total_baris` untuk tiap baris baru.
- **Loop Dalam**: Bertanggung jawab untuk mengontrol kolom ($j$) dari $1$ sampai $n$, menghitung nilai perkalian $i \times j$, serta mencetak tabel angka secara mendaftar ke samping.
- **Akumulator**: 
  - `total_baris`: Menjumlahkan seluruh hasil perkalian pada satu baris tertentu.
  - `total_semua`: Menjumlahkan keseluruhan hasil perkalian dari seluruh baris dalam tabel.
- **Counter**: 
  - `count_genap`: Menghitung banyaknya hasil perkalian $i \times j$ yang bernilai genap.

## Hasil Pengujian

| Input ($n$) | Hasil yang Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :---: |
| `1` | Total semua = 1, Banyak genap = 0 | Total semua = 1, Banyak genap = 0 | Lolos |
| `2` | Total semua = 9, Banyak genap = 3 | Total semua = 9, Banyak genap = 3 | Lolos |
| `3` | Total semua = 36, Banyak genap = 5 | Total semua = 36, Banyak genap = 5 | Lolos |

## Analisis Efisiensi
Badan loop dalam berjalan sebanyak **$n^2$ kali** (atau $n \times n$ kali). 
- Jika $n = 1$, loop dalam berjalan $1 \times 1 = 1$ kali.
- Jika $n = 2$, loop dalam berjalan $2 \times 2 = 4$ kali.
- Jika $n = 3$, loop dalam berjalan $3 \times 3 = 9$ kali.

Hal ini menunjukkan bahwa kompleksitas waktu dari algoritma *nested loop* ini adalah $\mathcal{O}(n^2)$ (kuadratik).

## Refleksi
- **Kesalahan yang ditemukan**: Variabel akumulator `total_baris = 0` ditaruh di luar/sebelum loop luar, sehingga nilainya terus bertambah dan tidak di-reset di setiap baris baru.
- **Cara memperbaikinya**: Memindahkan inisialisasi `total_baris = 0` ke dalam loop luar tepat sebelum loop dalam dimulai, sehingga nilainya kembali menjadi $0$ setiap kali berpindah ke baris baru.