'''
Nurani Syahidah (2200462)
Pendidikan Ilmu Komputer A 2022


Program integral : 
1. Metode Pias (Kaidah Trapesium)
2. Metode Pias (Kaidah Titik Tengah)
3. Metode Newton Cotes (Kaidah Simpson 1/3)
'''
import math

#Fungsi untuk menhitung Metode Pias (Kaidah Trapesium)
def pias_trapesium(f, a, b, h):
    n = int((b - a) / h)
    result = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        result += 2 * f(x_i)

    return (h / 2) * result

#Fungsi untuk menhitung Metode Pias (Kaidah Titik Tengah)
def pias_titik_tengah(f, a, b, h):
    n = int((b - a) / h)
    result = 0

    for i in range(1, n + 1):
        x_i = a + (i - 0.5) * h
        result += f(x_i)

    return h * result

#Fungsi untuk menhitung Metode Newton Cotes (Kaidah Simpson 1/3)
def simpson_1_3(f, a, b, h):
    n = int((b - a) / h)

    if n % 2 != 0:
        raise ValueError("Jumlah subinterval harus genap!")

    result = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            result += 2 * f(x_i)
        else:
            result += 4 * f(x_i)

    return (h / 3) * result

# Input dari pengguna
a = float(input("Batas bawah integral (a): "))
b = float(input("Batas atas integral (b): "))
h = float(input("Nilai h: "))

# Meminta pengguna untuk memasukkan fungsi integrand
fungsi_input = input("Fungsi integral f(x): ")
# Menggantikan nilai "e" dengan math.e
fungsi_input = fungsi_input.replace('e', str(math.e))
# Evaluasi string fungsi_input menjadi objek fungsi menggunakan fungsi eval
fungsi_integrasi = lambda x: eval(fungsi_input)

# Memanggil fungsi untuk menghitung integral
hasil_trapesium = pias_trapesium(fungsi_integrasi, a, b, h)
hasil_titik_tengah = pias_titik_tengah(fungsi_integrasi, a, b, h)
hasil_simpson_1_3 = simpson_1_3(fungsi_integrasi, a, b, h)

# Menampilkan hasil
print(f"\nHasil integral menggunakan metode Pias (trapesium): {hasil_trapesium}")
print(f"Hasil integral menggunakan metode Pias (titik tengah): {hasil_titik_tengah}")
print(f"Hasil integral menggunakan metode Newton-Cotes (Simpson 1/3): {hasil_simpson_1_3}")
