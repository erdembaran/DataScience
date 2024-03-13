import pandas as pd
import numpy as np

health_data = pd.read_csv('../csv/dataset1.csv', header= 0, sep = ";")

health_data.dropna(inplace = True)

health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

Max_Pulse = health_data["Max_Pulse"]

percentile10 = np.percentile(Max_Pulse, 10)

print(percentile10)
