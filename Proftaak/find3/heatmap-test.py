import numpy as np
import matplotlib.pyplot as plt



x = np.random.randn(2, )
y = np.random.randn(2,1000,30000)

plt.hist2d(x, y, bins=100)
plt.show()