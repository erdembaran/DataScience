import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

health_data = pd.read_csv('../csv/dataset1.csv', header= 0, sep = ";")

health_data.dropna(inplace = True)

health_data['Average_Pulse'] = health_data['Average_Pulse'].astype(float)
health_data['Calorie_Burnage'] = health_data['Calorie_Burnage'].astype(float)


x = health_data['Average_Pulse']
y = health_data['Calorie_Burnage']

slope, intercept = np.polyfit(x, y, 1)

print(slope, intercept)
