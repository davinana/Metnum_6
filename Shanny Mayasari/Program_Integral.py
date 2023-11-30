import numpy as np

# Fungsi yang ingin diintegralkan
def f(x):
    return np.sin(x)

# Metode trapesium untuk menghitung integral
def metode_trapesium(func, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        integral += func(a + i * h)
    integral *= h
    return integral

# Metode Simpson 1/3 untuk menghitung integral
def metode_simpson(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("n harus genap untuk metode Simpson 1/3")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return integral

# Metode titik tengah untuk menghitung integral
def metode_titikTengah(func, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_mid = (a + h * (i + 0.5))
        integral += func(x_mid)
    integral *= h
    return integral

# Batas integral dan jumlah subinterval (n)
a = 0  # Batas bawah
b = np.pi  # Batas atas
n = 100  # Jumlah subinterval

# Hitung integral menggunakan metode trapesium
integral_trapesium = metode_trapesium(f, a, b, n)
print(f"Hasil integral dengan metode trapesium: {integral_trapesium}")

# Hitung integral menggunakan metode Simpson 1/3
integral_simpson = metode_simpson(f, a, b, n)
print(f"Hasil integral dengan metode Simpson 1/3: {integral_simpson}")

# Hitung integral menggunakan metode titik tengah
integral_titikTengah = metode_titikTengah(f, a, b, n)
print(f"Hasil integral dengan metode titik tengah: {integral_titikTengah}")
