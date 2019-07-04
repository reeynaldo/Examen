import numpy as np
import matplotlib.pyplot as plt
def biseccion(f,x1,x2,t):

    return f(x - np.sin(x))

    if f(x1) * f(x2)  < 0 :
        xr = x1
        while abs(f(xr)) > t:
            xr = (x1 + x2) / 2

            if f(x1) * f(xr) < 0:
                x1 = xr
            else:
                x0 = xr
        return xr
    else:
        return "No hay cambio de signo"

