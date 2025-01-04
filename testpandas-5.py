import pandas as pd

coffee = pd.read_csv("./warmup-data/coffee.csv")
print(coffee.head())

### iat & at

print(coffee.Day)


### sort values
# -> none work line :  print(coffee.sort_values(['Units Sold', 'Coffee Type'], ascending=[False]))


### use 'for' for coffee

for index, row in coffee.iterrows():
    print(index)
    print(row)
    print("\n\n\n\n")

## or custom datas

for index, row in coffee.iterrows():
    print(index)
    print(row["Units Sold"])
    print("\n\n\n\n")


### Filtering data

bios = pd.read_csv('./data/bios.csv')

# how it syntaxis ->  bios.loc[bios['height_cm']>215 #parametr equalizing, ['name', 'height_cm'#like columns we choosed]]
print(bios.loc[bios['height_cm']>215, ['name', 'height_cm']])

print(bios[(bios['height_cm']>215) & (bios['born_country'] == 'USA')])


## FIND BY NEXT STRUCTURE
# in here "|" means or operator
print([bios['name'].str.contains("keith|patrick", case = False)])

##FILTERING DATA QUERY FUNCTIONS

print(bios.query("born_country == 'USA'"))
print(bios.query("born_country == 'USA' and born_city == 'Seattle' "))