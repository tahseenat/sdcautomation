import pandas as pd

file_name = 'Database.csv'
data = pd.read_csv(file_name, encoding="ISO-8859-1", usecols=range(0, 1))
data.insert(1, "Flag", 0)
data.to_csv(file_name, index=False)
print("Success")
