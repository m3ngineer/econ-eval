import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sy

def S(q):
    return (q**2)

def D(q):
    return (q - 20)**2

q = np.linspace(0, 16, 1000)

plt.plot(q, S(q), label = "Supply Curve")
plt.plot(q, D(q), label = "Demand Curve")
plt.plot(10, 100, 'o', markersize= 10)

plt.title("Supply and Demand")
plt.legend(frameon = False)
plt.xlabel("Quantity $q$")
plt.ylabel("Price")

q = sy.Symbol('q')
eq = sy.Eq(S(q), D(q))
sy.solve(eq)

# plt.show()

# Price discrimination
q = np.linspace(0, 16, 1000)
plt.figure(figsize = (9, 6))
plt.plot(q, D(q))
plt.fill_between(q, D(q), alpha = 0.1)
plt.title("Perfect Price Discrimination")

plt.xlabel("Quantity of good $q$")
plt.ylabel("Price of good $p$")
# ax = plt.axes()
# ax.annotate('Area Under Curve is Revenue \n$\int_0^{16}D(q) dq$', xy=(4, D(4)), xytext=(10, 250), arrowprops=dict(facecolor='black'))

plt.show()
