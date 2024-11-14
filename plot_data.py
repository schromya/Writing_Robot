import matplotlib
matplotlib.use("TkAgg")  # So works with display forwarding in docker

import matplotlib.pyplot as plt
import numpy as np

t = np.array([0, 1, 2, 3])
q0 = np.array([0, 1, 3, 4])

plt.scatter(t, q0)
plt.show()