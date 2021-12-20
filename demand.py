import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

demand1 = np.arange(1000,200,-125)
price1 = np.arange(500,1200,100)

demand2 = np.arange(1600,800,-125)
price2 = np.arange(400,1100,100)

plt.plot(demand1, price1)
plt.plot(demand2, price2)

plt.show()
