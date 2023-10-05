#Program metode Newton Raphson untuk menyelesaikan fungsi non-linear, hasil modifikasi dari contoh yang diberikan
import matplotlib.pyplot as plt
import numpy as np

# Fungsi
def f(x):
    return x**2 - 2*x - 8

# Turunan fungsi (ganti dengan metode numerik jika diperlukan)
def g(x):
    return 2*x - 2

# Metode Newton-Raphson
def newtonRaphson(x0, e, N):
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('dibagi 0 error')
            break
        x1 = x0 - f(x0) / g(x0)
        print(f'Iterasi-{step}, x1 = {x1:.6f} dan f(x1) = {f(x1):.6f}')
        x0 = x1
        step += 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print(f'\nakar yang dibutuhkan: {x1:.8f}')
    else:
        print('\ntidak konvergen')

# Fungsi untuk memilih metode
def choose_method():
    print("Pilih Metode:")
    print("1. Newton-Raphson")
    print("2. Metode Bisection")
    choice = input("Masukkan pilihan: ")
    return choice

# Fungsi untuk memasukkan input dari pengguna
def get_user_input():
    x0 = float(input('Masukkan perkiraan awal (x0): '))
    e = float(input('Masukkan perkiraan error (e): '))
    N = int(input('Masukkan jumlah step (N): '))
    return x0, e, N

# Fungsi untuk menampilkan grafik fungsi
def plot_function():
    x = np.linspace(-10, 10, 400)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Grafik Fungsi')
    plt.grid(True)
    plt.show()

# Main program
method = choose_method()
x0, e, N = get_user_input()

if method == '1':
    newtonRaphson(x0, e, N)
elif method == '2':
    print("Metode Bisection belum diimplementasikan")  # Implementasi Metode Bisection disini
else:
    print("Pilihan tidak valid")

# Tampilkan grafik fungsi jika diinginkan
plot_choice = input("Apakah Anda ingin melihat grafik fungsi? (y/n): ")
if plot_choice.lower() == 'y':
    plot_function()
