import pandas as pd


coffee = pd.read_csv("./warmup-data/coffee.csv")
print(coffee.head())


#read olypics
result = pd.read_parquet('./data/results.parquet')
print(result.head())

#read excel
olympics_data = pd.read_excel('./data/olympics-data.xlsx')
print(olympics_data.head())

#give sheets name
some_olypics_data = pd.read_excel('./data/olympics-data.xlsx',sheet_name="results")
print(some_olypics_data.head())

#how to convert to csv,parquet,excel, e.t.c
bios = pd.read_csv('./data/bios.csv')
print(bios.to_csv())
print(bios.to_parquet())
print(bios.to_excel())


