#No 1.a. f(x) = x^3 - 2x + 1
import numpy as np #panggil Library

 #fungsi metode bagi dua
def my_bisection(f, a, b, e): #fungsi metode bagi dua
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b') 
    m = (a + b)/2 
    if np.abs(f(m)) < e:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f,m,b,e)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f,a,m,e) 

#definisikan f(x) = x^3 - 2x + 1
f = lambda x: x**3 - 2*x + 1 

#Memanggil fungsi metode bagi dua
c = my_bisection(f, -2, 2, 0.01) 
print("c = ", c)
print("f(c) = ", f(c))
