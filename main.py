import math
import os

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

import config
import work_with_files
from Generator import Generator
from Model import Model
from observation import Observation


def get_color_for_plot(temperature):
    try:
        return config.temperature_to_color[temperature]
    except KeyError as e:
        raise ValueError('Undefined unit: {}'.format(e.args[0]))


def get_time_grid(lenght, h=100):
    time_grid = []
    for i in range(lenght):
        time_grid.append(h + i * h)
    return time_grid


def plot_trend(lenght, temperature, a, e, r, color="black"):
    trend_points = []

    for point in range(lenght):
        trend_points.append(a * math.exp(-e / (temperature * r)) * point * 100)

    plt.plot(trend_points, color=color)


def work_with_data():
    files = work_with_files.find_files(os.getcwd(), ".txt")
    lasers_data = []
    tmp = []
    T = [70 + 273.2] * 3 + [80 + 273.2] * 5 + [90 + 273.2] * 5
    for file in files:
        current_sample = work_with_files.get_sample(file)
        for value in current_sample:
            tmp.append(Observation(time=value.split("\t")[0], value=value.split("\t")[1]))
        lasers_data.append(work_with_files.centring_value(tmp))
        tmp = []
    return lasers_data, T


a = 1000
e = 0.5
T = [70 + 273.2] * 5 + [80 + 273.2] * 5 + [90 + 273.2] * 5
time_grid_generated = get_time_grid(300, 108)
generator = Generator(sigma=2, a=a, e=e,
                      temperature_list=T, time_grid=time_grid_generated)
# sample = generator.generate_sample()
sample, T = work_with_data()
model = Model(sample=sample, time_grid=time_grid_generated, temperature_list=T)
# 2.46324115e+00 8.12126307e+02 5.12889769e-01]
# [  2.02811803 499.52034217   0.5008919 ]
# [0.00375599 0.00202305 0.12227499]
# model.f([2, 500, 0.5])

result = opt.minimize(model.f, np.array([10, 2]), method='nelder-mead')
print(result.x)


z = []
i = 0
for obs in sample:
    z.append([0])
    for point in obs:
        sum = point + z[i][len(z[i]) - 1]
        z[i].append(sum)
    i = i + 1

_linestyle = ['-', '-', '-', '-', '-', '--', '--', '--', '--', '--', '-.', '-.', '-.', '-.', '-.']

for i in range(1, len(z)):
    plt.plot(z[i], color=get_color_for_plot(T[i]), linestyle=_linestyle[i])

blue_patch = mpatches.Patch(color=(0, 0, 1), label="323 К")
green_patch = mpatches.Patch(color=(0, 1, 0), label="333 К")
red_patch = mpatches.Patch(color=(1, 0, 0), label="343 К")
plt.legend(handles=[blue_patch, green_patch, red_patch])
plt.title(f"a={generator.a} sigma={generator.sigma} e={generator.e}")

first = []
second = []
third = []
# plot_trend(80, T[0], generator.a, generator.e, generator.r)
# plot_trend(80, T[5], generator.a, generator.e, generator.r)
# plot_trend(80, T[10], generator.a, generator.e, generator.r)

plot_trend(80, T[0], result.x[0], result.x[1], generator.r, (0, 0, 1))
plot_trend(80, T[5], result.x[0], result.x[1], generator.r, (0, 1, 0))
plot_trend(80, T[10], result.x[0], result.x[1], generator.r, (1, 0, 0))

plt.grid(True)
plt.show()
