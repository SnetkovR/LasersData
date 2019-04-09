import math


class Model:
    r = 8.6173303 * 10 ** (-5)

    def __init__(self,
                 sample, temperature_list: list, time_grid: list):
        self.time_grid = time_grid
        tmp = []
        for temperature in temperature_list:
            tmp.append(temperature)

        self.temperature_list = tmp

        self.sample = sample

    def trend(self, temperature, e):
        return math.exp(- e / (self.r * temperature))

    def f(self, variables):
        # sigma = variables[0]
        a = variables[0]
        e = variables[1]

        n = len(self.sample)
        k = len(self.sample[0])

        first_part = -k * n \
                     # * math.log(sigma)
        second_part = -k * n * 0.5 * math.log(2 * math.pi)

        eq = first_part + second_part

        sum = 0

        for i in range(n):
            k = len(self.sample[i])
            for j in range(1, k):
                h_t = self.time_grid[j] - self.time_grid[j - 1]
                tmp = e / (self.r * self.temperature_list[i])
                eq_z = -pow((self.sample[i][j - 1] - a * math.exp(-tmp) * h_t), 2) \
                       / (2 * math.exp(-tmp) * h_t)
                eq_t = -0.5 * (-tmp + math.log(h_t))
                sum = sum + eq_z + eq_t
        eq = eq + sum
        print("Not Dead! A = {0} E = {1}, -eq = {2}".format(a, e, -eq))
        return -eq
