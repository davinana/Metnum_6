# Mendefinisikan fungsi
def f(x):
    return x**2-2*x-8
# Mendifinisikan fungsi derivatif
def g(x):
    return 2*x-2
# Mendefinisikan fungsi metode newtonRaphson
def newtonRaphson(x0,e,N):
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('dibagi 0 error')
            break
        #loop iterasi
        x1 = x0 - f(x0)/g(x0)
