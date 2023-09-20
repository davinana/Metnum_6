#N0.1b.f(x) = e^x - x
import numpy as np #panggil library

#fungsi metode bagi dua
def my_bisection(f, a, b, e):
  if np.sign(f(a)) == np.sign(f(b)):
    raise Exception('Tidak ada akar pada interval a dan b')
  m = (a + b)/2
  if np.abs(f(m)) < e:
    return m
  elif np.sign(f(a)) == np.sign(f(m)):
    return my_bisection(f, m, b, e)
  elif np.sign(f(b)) == np.sign(f(m)):
    return my_bisection(f, a, m, e)

#definisi fungsi f(x) = e^x - x

f = lambda x: np.exp(x) - x #definisikan fungsi soal menggunakan lambda
c = my_bisection(f, -2, 2, 0.01) #memanggil fungsi, dengan argumen yang diberikan
print("c = ", c)
print("f(c) = ", f(c))
