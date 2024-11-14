import matplotlib
matplotlib.use("TkAgg")  # So works with display forwarding in docker

# import matplotlib.pyplot as plt
# import numpy as np
# import time

# t = np.array([0, 1, 2, 3])
# q0 = np.array([1, 2, 3, 4])

# plt.ion()


# fig = plt.figure() 
# ax = fig.add_subplot(111) 
# line1, = ax.plot(t, q0, )

# for phase in np.linspace(0, 10*np.pi, 100): 
#     q0 = q0  + 1
#     print(q0)
#     line1.set_ydata(q0 ) 
#     fig.canvas.draw() 
#     fig.canvas.flush_events() 

import matplotlib.pyplot as plt 
import numpy as np 
  
x = np.linspace(0, 10*np.pi, 100) 
y = np.sin(x) 
  
plt.ion() 
fig = plt.figure() 
ax = fig.add_subplot(111) 
line1, = ax.plot(x, y, 'b-') 
  
for phase in np.linspace(0, 10*np.pi, 100): 
    line1.set_ydata(np.sin(0.5 * x + phase)) 
    fig.canvas.draw() 
    fig.canvas.flush_events() 