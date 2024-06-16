import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
binomial = rng.binomial(10, 0.5, 1000)
normal = rng.normal(0, 0.25, 1000)
uniform = rng.uniform(-1, 1, 1000)

fig, axs = plt.subplots(1, 3, sharey=True)

axs[0].hist(binomial)
axs[1].hist(normal)
axs[2].hist(uniform)

plt.show()