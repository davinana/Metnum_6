#Metode Newton-Raphson

import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan fungsi yang akan dicari akarnya
def fungsi(x):
    return eval(persamaan)

# Mendefinisikan turunan fungsi
def turunan_fungsi(x):
    return eval(derivative)

# Mendefinisikan metode Newton-Raphson
def metode_newton_raphson(f, df, x0, tol, max_iter):
    iterasi = []
    x = x0
    for i in range(max_iter):
        iterasi.append(x)
        x = x - f(x) / df(x)
        if np.abs(f(x)) < tol:
            return x, iterasi
    return x, iterasi

# Input persamaan, turunan persamaan, tebakan awal, ketelitian, dan jumlah maksimum iterasi dari pengguna
persamaan = input("Masukkan persamaan fungsi (contoh: 'x**2 - 2*x - 8'): ")
derivative = input("Masukkan turunan fungsi (contoh: '2*x - 2'): ")
x0 = float(input("Masukkan tebakan awal (x0): "))
toleransi = float(input("Masukkan ketelitian (contoh: 0.001, 3 angka dibelakang koma): "))
max_iterasi = int(input("Masukkan jumlah maksimum iterasi: "))

# Mencari akar dengan metode Newton-Raphson
akar, iterasi = metode_newton_raphson(fungsi, turunan_fungsi, x0, toleransi, max_iterasi)

# Menampilkan hasil akar dan iterasi
print("Akar hampiran:", akar)
print("Iterasi yang diperlukan:", len(iterasi))

# Membuat array nilai x untuk menggambar grafik
x = np.linspace(x0 - 2, x0 + 2, 400)  # Sesuaikan rentang x sesuai dengan tebakan awal
y = [fungsi(xi) for xi in x]

# Menampilkan grafik fungsi
plt.plot(x, y, label=f'f(x) = {persamaan}')
plt.axhline(0, color='red', linestyle='--', linewidth=0.7, label='y = 0')
plt.scatter(iterasi, [fungsi(xi) for xi in iterasi], color='green', label='Iterasi', zorder=5)
plt.annotate(f'Akar hampiran: {akar:.6f}', (akar, fungsi(akar)), color='blue')

# Konfigurasi grafik
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik fungsi f(x) dengan Iterasi Metode Newton-Raphson')
plt.grid(True)
plt.legend()

# Menampilkan grafik
plt.show()
