import pandas as pd

data = {
    "name": ["cristiano", "lionel", "dusan", "edin", "karim"],
    "lastname": ["ronaldo", "messi", "tadic", "dzeko", "benzema"],
    "team": ["al-nassr", "miami", "fenerbahce", "fenerbahce", "al-ittihadx"],
}

df = pd.DataFrame(data)


print(df)