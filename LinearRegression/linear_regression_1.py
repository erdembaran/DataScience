import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('sales.csv')

months = data[['Months']]
                  
print(months)

sales = data[['Sales']]

print(sales)
