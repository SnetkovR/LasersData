import math
import random


class Generator:
    r = 8.6173303 * 10 ** -5
    sample = []

    def __init__(self, sigma, a, e, temperature_list, time_grid):
        self.time_grid = time_grid
        self.e = e
        self.a = a
        self.sigma = sigma
        self.sample = []

        tmp = []
        for temperature in temperature_list:
            tmp.append(temperature)

        self.temperature_list = tmp

    def trend(self, temperature):
        return math.exp(-self.e / (self.r * temperature))

    def generate_observation_for_one_object(self, temperature):
        z = []
        for i in range(1, len(self.time_grid)):
            delta_t = self.time_grid[i] - self.time_grid[i - 1]
            mu = self.a * self.trend(temperature) * delta_t
            sig = self.sigma * math.sqrt(self.trend(temperature) * delta_t)
            z.append(random.normalvariate(mu, sig))
        return z

    def generate_sample(self):
        for i in range(len(self.temperature_list)):
            delta_z = self.generate_observation_for_one_object(self.temperature_list[i])
            self.sample.append(delta_z)
        return self.sample
