import numpy as np
import matplotlib.pyplot as plt
#physical setup
g = 9.8
l = 1.0
damper = 0.1

#inital conditions
theta_0 = np.pi/2
theta_prime_0 = 50

# approximation parameters 
step_sz = 0.01
max_t = 100
def theta_2_prime(theta, theta_prime):
    global g, l, damper
    return -g/l*np.sin(theta) - damper*theta_prime



def get_theta(theta_0, theta_prime_0, step_sz, num_steps):
    theta = theta_0
    theta_prime = theta_prime_0
    theta_vals = [theta_0]
    theta_prime_vals = [theta_prime_0]
    for _ in range(num_steps - 1):
        theta_double_prime = theta_2_prime(theta, theta_prime)
        theta_prime = theta_prime + step_sz*theta_double_prime
        theta = theta + step_sz*theta_prime
        theta_vals.append(theta)
        theta_prime_vals.append(theta_prime)
    return theta_vals, theta_prime_vals

t = np.arange(0, max_t, step_sz)
theta_vals, theta_prime_vals = get_theta(theta_0, theta_prime_0, step_sz, len(t))
plt.plot(t, theta_vals)
plt.show()




