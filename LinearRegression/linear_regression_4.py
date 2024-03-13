import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('../csv/sales.csv')
months = data[['Months']]
sales = data[['Sales']]

x_train, x_test,y_train,y_test = train_test_split(months,sales,test_size=0.33, random_state=0)

lr = LinearRegression()

lr.fit(x_train, y_train)

