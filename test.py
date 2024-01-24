import numpy as np
from methods import newtons_method
import matplotlib.pyplot as plt

def y_prime(y, t):
    return np.sqrt(y*t)

y_0 = 1
t_0 = 0
step_sz = 0.01
max_t = 500
y_vals, t_vals = newtons_method(y_0, t_0, step_sz, max_t, y_prime)
plt.plot(t_vals, y_vals)
plt.show()
