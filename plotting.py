import matplotlib.pyplot as plt
from computation import *


def show_graphs(source: list[float]):
    plot_empirical_dist(source)
    bar_interval_stat_dist(source)
    polygon_interval_stat_dist(source)


def plot_empirical_dist(source: list[float]):
    series = stat_series(source)
    for (val1, key1), (val2, key2) in zip(series, series[1:]):
        plt.plot([val1, val2],
                 [empirical_dist(source, val1),
                  empirical_dist(source, val1)])
    plt.title('График эмпирической функции распределения')
    plt.show()


def bar_interval_stat_dist(source: list[float]):
    int_st_d = interval_stat_dist(source)
    xs = [key for key, val in int_st_d]
    ys = [val for key, val in int_st_d]
    plt.bar(xs, ys, color=["blue", "indigo"], edgecolor=["indigo", "blue"], width=0.4, linewidth=3)
    plt.title('Гистограмма частот группированной выборки')
    plt.show()


def polygon_interval_stat_dist(source: list[float]):
    int_st_d = interval_stat_dist(source)
    xs = [key for key, val in int_st_d]
    ys = [val for key, val in int_st_d]
    plt.plot(xs, ys)
    plt.title('Полигон частот группированной выборки')
    plt.show()
