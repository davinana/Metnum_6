def f(x):
    # Fungsi yang ingin dihitung turunannya
    return x**3 - 2*x - 5

def numerical_derivative(f, x, h=0.0001):
    # Menghitung turunan numerik menggunakan metode beda hingga (finite difference)
    derivative = (f(x + h) - f(x)) / h
    return derivative

# Titik di mana turunan akan dihitung
x_value = 2

# Menghitung turunan pada titik x_value
result = numerical_derivative(f, x_value)
print(f"Turunan pada x = {x_value} adalah: {result}")
