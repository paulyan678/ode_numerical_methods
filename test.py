import numpy as np
from methods import newtons_method, improved_newtons_method
import matplotlib.pyplot as plt

def y_prime(y, t):
    return y

y_0 = 1
t_0 = 0
step_sz = 0.1
max_t = 10
y_vals_newton, t_vals_newton = newtons_method(y_0, t_0, step_sz, max_t, y_prime)
y_vals_improved_newton, t_vals_improved_newton = improved_newtons_method(y_0, t_0, step_sz, max_t, y_prime)
plt.plot(t_vals_newton, y_vals_newton, label="Newton's Method")
plt.plot(t_vals_improved_newton, y_vals_improved_newton, label="Improved Newton's Method")
plt.legend()
plt.show()
