from computation import *


# Округление для исправления неточностей
def to_fixed(num, digits=0):
    return f"{num:.{digits}f}"


def print_parameters(source: list[float]):
    print("*** Вариационный ряд ***")
    print(source)
    print()

    print("*** Экстремальные значения ***")
    print("Минимум:", extreme_values(source)[0], "| Максимум:", extreme_values(source)[1])
    print()

    print("*** Размах выборки ***")
    print("R =", to_fixed(sampling_range(source), 2))
    print()

    print("*** Мода ***")
    print("M*o =", mode(source))
    print()

    print("*** Медиана ***")
    print("M*e =", to_fixed(median(source), 3))
    print()

    print("*** Мат. ожидание ***")
    print("M =", to_fixed(math_expectation(source), 3))
    print()

    print("*** Дисперсия ***")
    print("D =", dispersion(source))
    print()

    print("*** Среднеквадратичное отклонение ***")
    print("s =", deviation(source))
    print()

    print("*** Эмпирическая функция распределения ***")
    series = stat_series(source)
    for i, (val, count) in enumerate(series):
        if i == 0:
            print(f"x <= {val}: {empirical_dist(source, val)}")
        else:
            prev_val = series[i - 1][0]
            print(f"{prev_val} < x <= {val}: {empirical_dist(source, val)}")
        last_val = series[-1][0]
        print(f"{last_val} < x: {empirical_dist(source, float('inf'))}")
