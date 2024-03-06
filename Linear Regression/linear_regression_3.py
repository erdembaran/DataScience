import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('sales.csv')
months = data[['Months']]
sales = data[['Sales']]

x_train, x_test,y_train,y_test = train_test_split(months,sales,test_size=0.33, random_state=0)

print(x_train)
print(x_test)
