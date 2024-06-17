import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

msds_data = pd.read_csv("MSDS-Orientation-Computer-Survey(in).csv")

histCPUCore = msds_data.hist(column="CPU Number of Cores (int)", bins = 20, color = "#D42121", label = "CPU Number of Cores")
plt.show()

histCPUCycle = msds_data.hist(column="CPU Cycle Rate (in GHz)", bins = 5, color = "#D42121", label = "CPU Cycle Rate")
plt.show()

histRAM = msds_data.hist(column="RAM (in GB)", bins = 50, color = "#D42121", label = "RAM")
plt.show()

histDrive = msds_data.hist(column="Hard Drive Size (in GB)", bins = 50, color = "#D42121", label = "Hard Drive Size")
plt.show()