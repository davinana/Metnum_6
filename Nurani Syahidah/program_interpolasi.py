'''
Nurani Syahidah- 2200462
Pendidikan Ilmu Komputer A 2022
'''

def linear_interpolation(x_values, y_values, x_interpolate):
    n = len(x_values)
    
    if len(y_values) != n:
        raise ValueError("Jumlah nilai y harus sama dengan jumlah nilai x")
    
    for i in range(n-1):
        if not (x_values[i] < x_interpolate <= x_values[i+1]):
            continue
        
        # Interpolasi linier
        x0, y0 = x_values[i], y_values[i]
        x1, y1 = x_values[i+1], y_values[i+1]
        
        interpolated_value = y0 + (y1 - y0) * (x_interpolate - x0) / (x1 - x0)
        return interpolated_value
    
    raise ValueError(f"Tidak dapat melakukan interpolasi untuk nilai x={x_interpolate}")

# Input nilai x dan y
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 25, 30, 35]

# Input nilai x yang ingin diinterpolasi
x_interpolate = float(input("Masukkan nilai x yang ingin diinterpolasi: "))

# Melakukan interpolasi
result = linear_interpolation(x_values, y_values, x_interpolate)

# Menampilkan hasil interpolasi
print(f"Hasil interpolasi untuk x={x_interpolate}: {result}")
