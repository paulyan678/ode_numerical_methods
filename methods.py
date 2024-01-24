import numpy as np


def newtons_method(y_0, t_0, step_sz, max_t, diff_eq):
    """
    :param y_0: Initial value of y
    :param t_0: Initial value of t
    :param step_sz: Step size
    :param max_t: Maximum value of t
    :param diff_eq: Differential equation
    :return: numpy array of y values at each steps
    """
    y = y_0
    t = t_0
    y_values = [y_0]
    t_vals = [t_0]
    while t < max_t:
        y = y + step_sz * diff_eq(y, t)
        y_values.append(y)
        t_vals.append(t)
        t += step_sz
    return np.array(y_values), np.array(t_vals)

def improved_newtons_method(y_0, t_0, step_sz, max_t, diff_eq):
    """
    :param y_0: Initial value of y
    :param t_0: Initial value of t
    :param step_sz: Step size
    :param max_t: Maximum value of t
    :param diff_eq: Differential equation
    :return: numpy array of y values at each steps
    """
    y = y_0
    t = t_0
    y_values = [y_0]
    t_vals = [t_0]
    while t < max_t:
        cur_slope = diff_eq(y, t)
        y_peak = y + step_sz * cur_slope
        peak_slope = diff_eq(y_peak, t + step_sz)
        y = y + step_sz * (cur_slope + peak_slope) / 2
        y_values.append(y)
        t_vals.append(t)
        t += step_sz
    return np.array(y_values), np.array(t_vals)


