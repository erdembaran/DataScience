import pandas as pd

data = {
    "name": ["cristiano", "lionel", "dusan", "edin", "luka"],
    "lastname": ["ronaldo", "messi", "tadic", "dzeko", "modric"],
    "team": ["al-nassr", "miami", "fenerbahce", "fenerbahce", "real madrid"],
}

df = pd.DataFrame(data)


print(df)