import numpy as np

def jalanLU(A,b):
    n = len(A)
    L = np.zeros((n,n))
    for i in range(n):
        L[i][i] = 1

    for k in range(n-1):
        if A[k][k] == 0:
            for s in range(n):
                v = A[k][s]
                u = A[k+1][s]
                A[k][s] = u
                A[k+1][s] = v

        for j in range(k+1,n):
            m = A[j][k]/A[k][k]
            L[j][k] = m
            for i in range(n):
                A[j][i] = A[j][i] - m*A[k][i]

    print('Matriks L')
    print(L)

    print('Matriks U')
    print(A)

    y = np.zeros((n,1))
    y[0][0] = b[0][0]/L[0][0]
    for j in range(1,n):
        S = 0
        for i in range(j):
            S = S + y[i][0]*L[j][i]
        y[j][0] = b[j][0] - S

    x = np.zeros((n,1))
    x[n-1][0] = y[n-1][0]/A[n-1][n-1]
    for j in range(n-2,-1,-1):
        S = 0
        for i in range(j+1,n):
            S = S + A[j][i]*x[i][0]
        x[j][0] = (y[j][0] - S)/A[j][j]

    print('Solusi:\n')
    for i in range(n):
        print(f'X{i+1} = {x[i]}')

# Meminta input matriks A dari pengguna
A = []
n = int(input("Masukkan ukuran matriks (n x n): "))
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    row = []
    for j in range(n):
        elem = float(input(f"A[{i+1}][{j+1}]: "))
        row.append(elem)
    A.append(row)

#input matriks b dari user
b = []
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    elem = float(input(f"B[{i+1}]: "))
    b.append([elem])
  
jalanLU(np.array(A), np.array(b))
