import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 9999

df = pd.read_csv('dataset2.csv')

print(df.to_string())