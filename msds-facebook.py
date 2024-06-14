import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

msds_data = pd.read_csv("MSDS-Orientation-Computer-Survey(in).csv")

hist = msds_data.hist(column="CPU Number of Cores (int)", bins = 5, color = "#D42121", label = "CPU Number of Cores")
plt.xlabel('CPU Cores')
plt.ylabel('Frequency')
plt.show()