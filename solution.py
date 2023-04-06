import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 5459656416 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    std_dev = (np.amax(x) - np.exp(1)) / (2 * norm.ppf((1 - p) / 2))
    margin_of_error = std_dev / np.sqrt(n)
    left_boundary = (np.mean(x) / 2) - margin_of_error
    right_boundary = (np.mean(x) / 2) + margin_of_error
    return (left_boundary, right_boundary)
