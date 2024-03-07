import pandas as pd

data = {
    "name": ["cristiano", "lionel", "dusan", "edin", "eden"],
    "lastname": ["ronaldo", "messi", "tadic", "dzeko", "hazard"],
    "university": ["ubc", "harvard", "ucberkeley", "oxford", "cambridge"],
}

df = pd.DataFrame(data)


print(df.loc[[0,1,2,3,4], ["name", "university"]])