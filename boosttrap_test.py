import numpy as np

from generator import Generator
from utils import get_time_grid, get_bootstrap_samples
from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt


def theoretical(gen, n):
    return [np.argmax(np.array(sample) > 1.5) for sample in gen.generate_sample(n)]


gen = Generator(
    sigma=1,
    time_grid=get_time_grid(200, 1),
    beta_0=1
)
sample = gen.generate_sample(1)
sam_2 = theoretical(gen, 300)
samples = [np.argmax(sample > 1.5) for sample in get_bootstrap_samples(np.array(sample), 1000)]
ecdf = ECDF(samples)
plt.plot(
    ecdf.x,
    ecdf.y,
    color='b'
)

ecdf_2 = ECDF(sam_2)
plt.plot(
    ecdf_2.x,
    ecdf_2.y,
    color='r'
)
plt.show()

