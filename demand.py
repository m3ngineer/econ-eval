import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sp

def S(q):
    return (q**2)

def D(q):
    return (q - 20)**2

q = np.linspace(0, 16, 1000)

plt.plot(q, S(q), label = "Supply Curve")
plt.plot(q, D(q), label = "Demand Curve")
plt.title("Supply and Demand")
plt.legend(frameon = False)
plt.xlabel("Quantity $q$")
plt.ylabel("Price")

q = sy.Symbol('q')
eq = sy.Eq(S(q), D(q))
sy.solve(eq)

plt.show()
