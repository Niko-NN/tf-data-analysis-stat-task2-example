import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 5459656416 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    t_i = 2  # время измерения
    v = x / t_i  # вычисление выборочных значений скорости
    n = len(v)
    v_mean = np.mean(v)  # выборочное среднее скорости
    s = np.sqrt(np.sum((v - v_mean) ** 2) / (n - 1))  # выборочное стандартное отклонение
    norm_alpha_2 = norm.ppf(1 - p / 2, n - 1)  # квантиль распределения Стьюдента
    a_hat = np.sum(v * t_i) / np.sum(t_i ** 2)  # оценка коэффициента ускорения
    left_bound = a_hat - norm_alpha_2 * s / np.sqrt(np.sum(t_i ** 2))
    right_bound = a_hat + norm_alpha_2 * s / np.sqrt(np.sum(t_i ** 2))
    return (left_bound, right_bound)
