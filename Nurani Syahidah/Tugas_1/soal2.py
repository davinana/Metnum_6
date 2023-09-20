#NO.2
#1. Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n
#2. Buatlah modifikasi agar user dapat menginputkan fungsi maupun batas akar dan galatnya
#3. Buatlah modifikasi agar akarnya dapat ditampilkan dalam bentuk grafik

import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan fungsi yang akan dicari akarnya
def fungsi(x):
    return eval(persamaan)

# Mendefinisikan metode bisection
def metode_bisection(f, a, b, tol, max_iter):
    iterasi = []
    for _ in range(max_iter):
        c = (a + b) / 2.0
        iterasi.append(c)
        if np.abs(f(c)) < tol:
            return c, iterasi
        elif f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
    return (a + b) / 2.0, iterasi

# Input persamaan, interval, jumlah maksimum iterasi, dan ketelitian dari pengguna
persamaan = input("Masukkan persamaan fungsi (contoh: 'x**2 - 2*x - 8'): ")
a = float(input("Masukkan batas bawah interval (a): "))
b = float(input("Masukkan batas atas interval (b): "))
toleransi = float(input("Masukkan ketelitian (contoh: 0.001, 3 angka dibelakang koma): "))
max_iterasi = int(input("Masukkan jumlah maksimum iterasi: "))

# Mencari akar dengan metode bisection
akar, iterasi = metode_bisection(fungsi, a, b, toleransi, max_iterasi)

# Menampilkan hasil akar dan iterasi
print("Akar hampiran:", akar)
print("Iterasi yang diperlukan:", len(iterasi))

# Membuat array nilai x untuk menggambar grafik
x = np.linspace(a, b, 400)
y = [fungsi(xi) for xi in x]

# Menampilkan grafik fungsi
plt.plot(x, y, label=f'f(x) = {persamaan}')
plt.axhline(0, color='red', linestyle='--', linewidth=0.7, label='y = 0')
plt.scatter(iterasi, [fungsi(xi) for xi in iterasi], color='green', label='Iterasi', zorder=5)
plt.annotate(f'Akar hampiran: {akar:.6f}', (akar, fungsi(akar)), color='blue')

# Konfigurasi grafik
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik fungsi f(x) dengan Iterasi Metode Bisection')
plt.grid(True)
plt.legend()

# Menampilkan grafik
plt.show()
