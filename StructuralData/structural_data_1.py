import pandas as pd
import json

# Read the JSON file into a dictionary
with open("dataset2.json", "r") as json_file:
    data_from_file = json.load(json_file)

# Create a DataFrame from the loaded data
df = pd.DataFrame(data_from_file)
# Print the DataFrame
print(df)
