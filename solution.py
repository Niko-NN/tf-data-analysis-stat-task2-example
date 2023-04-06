import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import t

chat_id = 5459656416 # Ваш chat ID, не меняйте название переменной

def acceleration_ci(p, x):
    n = len(x)
    s = np.std(x, ddof=1) 
    t_value = t.ppf(1 - (1 - p) / 2, n - 1)
    a = 2 / (t_value ** 2 * 2)
    left = np.mean(x) - t_value * s / np.sqrt(n) * a
    right = np.mean(x) + t_value * s / np.sqrt(n) * a
    return (left, right)
