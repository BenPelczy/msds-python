import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
binomial = rng.binomial(10, 0.5, 1000000)
normal = rng.normal(10, 0.5, 1000000)

fig, axs = plt.subplots(1, 2, sharey=True)

axs[0].hist(binomial)
axs[1].hist(normal)

plt.show()