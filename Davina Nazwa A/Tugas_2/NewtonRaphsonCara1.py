#Menginisialisai fungsi untuk menghitung f(xi), f'(xi), xi, dan e
def newton_raphson(f, df, xi, e):
    print("Nilai xi: ", xi)
    if abs(f(xi)) < e:
        return xi
    else:
        xi = xi - f(xi)/df(xi)
        return newton_raphson(f, df, xi, e)

#Definisikan f(x), f'(x), dan nilai awal
fx = lambda x: ((x**2)+(3*x)-108)
f_prime = lambda x: 2*x + 3
n = float(input("Masukkan Nilai Aproksimaksi Awal: "))

#Pemanggilan fungsi Newton Raphson
estimate = newton_raphson(fx, f_prime, n, 1e-3)
print ("estimate = %.3f" % estimate)
