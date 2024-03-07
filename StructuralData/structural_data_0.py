import pandas as pd

data = {
    "name": ["cristiano", "lionel", "dusan", "edin", "luka"],
    "lastname": ["ronaldo", "messi", "tadic", "dzeko", "modric"],
    "team": ["al-nassr", "miami", "fenerbahce", "fenerbahce", "real madrid"],
}

df = pd.DataFrame(data)


print(df.loc[[0,1,2,3,4], ["name", "university"]])