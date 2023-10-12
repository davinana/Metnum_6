import numpy as np

def eliminasi_gaussian_partial(A, b):
    n = A.shape[0]
    C = np.c_[A, b]
    flag = 0

    for i in range(n-1):
        max_c, chosen_k = 0, i

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

def substitusi_mundur(T):
    n = T.shape[0]
    flag = 0
    X = np.zeros(n)
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

# Input matriks A dari pengguna
n = int(input("Masukkan ukuran matriks (n x n): "))
A = np.zeros((n, n))
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    for j in range(n):
        elem = float(input(f"A[{i+1}][{j+1}]: "))
        A[i, j] = elem

# Input matriks b dari pengguna
b = np.zeros((n, 1))
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    elem = float(input(f"B[{i+1}]: "))
    b[i, 0] = elem

T, err = eliminasi_gaussian_partial(A, b)

if err:
    print('Solusi tidak unik')
else:
    X, err = substitusi_mundur(T)
    if err:
        print('Solusi tidak unik')
    else:
        print('Solusi:')
        for i, val in enumerate(X):
            print(f"X{i+1} = {val}")
