'''
nurani syahidah - 2200462
Pendidikan Ilmu Komputer A 2022
'''
import numpy as np

def gaussian_partial(A, b):
    n = A.shape[0]
    C = np.c_[A, b.reshape(-1, 1)]
    flag = 0

    for i in range(n-1):
        max_c, chosen_k  = 0, i
        
        for k in range(i, n):
            if np.abs(C[k, i]) > max_c:
                max_c = np.abs(C[k, i])
                chosen_k = k

        if max_c == 0:
            flag = 1
            break

        if chosen_k != i:
            temp = C[i, :].copy()
            C[i, :] = C[chosen_k, :]
            C[chosen_k, :] = temp

        for j in range(i+1, n):
            c = C[j, i] / C[i, i]
            C[j, :] = C[j, :] - c * C[i, :]

    return C, flag

def backsubstitution(T):
    flag = 0
    n = T.shape[0]
    X = np.zeros((n))
    if T[n-1, n-1] == 0:
        flag = 1
    else:
        X[n-1] = T[n-1, n] / T[n-1, n-1]

        for i in range(n-2, -1, -1):
            s = 0
            for j in range(i+1, n):
                s += T[i, j] * X[j]

            X[i] = (T[i, n] - s) / T[i, i]

    return X, flag

# Meminta input matriks A dari pengguna
n = int(input("Masukkan ukuran matriks (n x n): "))
A = []
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    row = []
    for j in range(n):
        elem = float(input(f"A[{i+1}][{j+1}]: "))
        row.append(elem)
    A.append(row)

# Meminta input matriks b dari pengguna
b = []
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    elem = float(input(f"B[{i+1}]: "))
    b.append([elem])

T, err = gaussian_partial(np.array(A), np.array(b))

if err:
    print('Solusi tidak unik')
else:
    X, err = backsubstitution(T)
    if err:
        print('Solusi tidak unik')
    else:
        print('Solusi:')
        for i, val in enumerate(X):
            print(f"X{i+1} = {val}")
