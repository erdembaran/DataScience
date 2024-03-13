import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv('../csv/dataset1.csv', header= 0, sep = ";")

health_data.plot(x = "Average_Pulse", y = "Calorie_Burnage", kind = "line")

plt.show()