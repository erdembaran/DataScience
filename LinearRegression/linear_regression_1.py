import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../csv/sales.csv')  

months = data[['Months']]
                  
print(months)

sales = data[['Sales']]

print(sales)
