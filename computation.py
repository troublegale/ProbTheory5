from collections import Counter
from math import log2
from scipy import stats
import numpy


# Вариационный ряд (значения в порядке неубывания)
def variation_series(source: list[float]):
    return sorted(source)


# Экстремальные значения (минимум и максимум)
def extreme_values(source: list[float]):
    return min(source), max(source)


# Размах выборки
def sampling_range(source: list[float]):
    return max(source) - min(source)


# Мода
def mode(source: list[float]):
    return stats.mode(source)[0]


# Медиана
def median(source: list[float]):
    return numpy.median(source)


# Статистический ряд в виде пар [значение] - [количество его появлений]
# Составляется для вычисления мат. ожидания и дисперсии
def stat_series(source: list[float]):
    return [(key, val) for key, val in Counter(source).items()]


# Оценка мат. ожидания
def math_expectation(source: list[float]):
    return sum([key * val for (key, val) in stat_series(source)]) / len(source)


# Выборочная дисперсия
def dispersion(source: list[float]):
    math_exp = math_expectation(source)
    components = [count * (val - math_exp) ** 2 for (val, count) in stat_series(source)]
    return sum(components) / len(source)


# Среднеквадратичное отклонение
def deviation(source: list[float]):
    return dispersion(source) ** 0.5


# Исправленная дисперсия
def corrected_dispersion(source: list[float]):
    """Исправленная дисперсия"""
    me = math_expectation(source)
    d = 0
    for (elem, count) in stat_series(source):
        d += count * (elem - me) ** 2
    return d / (len(source) - 1)


# Исправленное среднеквадратичное отклонение
def corrected_deviation(source: list[float]):
    return corrected_dispersion(source) ** 0.5


# Эмпирическая функция распределения
def empirical_dist(source: list[float], x: float):
    count = 0
    for val in source:
        if val < x:
            count += 1
        else:
            break
    return count / len(source)


# Интервальный статистический ряд
def interval_stat_dist(source: list[float]):
    # формула Стерджиса
    h = (max(source) - min(source)) / (1 + log2(len(source)))
    first_x = source[0] - h / 2
    current_x = first_x
    interval = {current_x: 0}
    for val in source:
        if current_x <= val < current_x + h:
            interval[current_x] = interval.get(current_x, 0) + 1
        else:
            while current_x + h < val:
                current_x += h
                interval[current_x] = 0
            interval[current_x] = interval.get(current_x, 0) + 1
    return [(k, v / len(source)) for k, v in interval.items()]
