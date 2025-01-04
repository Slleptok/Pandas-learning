import pandas as pd




'''
# read sheets with matrix(Type csv)
# read sheets with matrix(Type parquet)
# read sheets with matrix(Type excel)
# give sheets name
# converting sheets type
'''
# read sheets with matrix(Type csv)
coffee = pd.read_csv('../warmup-data/coffee.csv')
print(coffee.head())

# read sheets with matrix(Type parquet)
result = pd.read_parquet('../data/results.parquet')
print(result.head())

# read sheets with matrix(Type excel)
olympics_data = pd.read_excel('../data/olympics-data.xlsx')

# give sheets name
some_olympics_data = pd.read_excel('./data/olympics-data.xlsx', sheet_name='results')
print(some_olympics_data.head())

# converting sheets type
bios = pd.read_csv('../data/bios.csv')
# and converting
# to_csv
print(bios.to_csv())

# to_excel
print(bios.to_excel())

# to_parquet
print(bios.to_parquet())

# to_sql
print(bios.to_sql())
# and also we can convert to rest data frame types


