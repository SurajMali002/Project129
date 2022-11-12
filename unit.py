import pandas as pd

df = pd.read_csv("Dwarf.csv")

df.columns

df.dtypes

df.head()

df = df.dropna()

df["Radius"] = 0.102763*df["Radius"]

df["Mass"] = df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

df["Mass"] = 0.000954588*df["Mass"]

df.head()

df.columns

df.to_csv("Dwarf1.csv")