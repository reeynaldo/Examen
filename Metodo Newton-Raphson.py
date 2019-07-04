def f(x):
    return x*4-10*x**3+3*x*2+x+23

def Df(x):
    return 4*x*3-30*x*2+6*x+1
x0=1

for Iteraccion in range (1,11):
    x1 = x0 - f(x0)/ Df(x0)
    e = abs(x1 - x0)
    x0 = x1
    print(x0)
