import pandas as pd
import numpy as np

bios = pd.read_csv('./data/bios.csv')
coffee = pd.read_csv("./warmup-data/coffee.csv")

###ADDING / REMOVING COLUMNS



##ADDING
coffee_new = coffee.copy()
coffee_new['price'] = 4.99

coffee['new_price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99 , 5.99)
print(coffee.head(13))



##REMOVING
#Rewiew columns
#print(coffee.drop(columns=['price']))

##WIEW
coffee = coffee[['Day','Coffee Type', 'Units Sold', 'new_price']]
print(coffee)

##ALSO ADDING
coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']

print(coffee.head())



##RENAME COLUMNS
# -> {'old value name':'new value name'}
coffee.rename(columns={'new_price':'price'})






###Lets continue the ADDING AND REMOVING

bios_new = bios.copy()
# here we adding the new column as "first_name" and adding his copy with modifier like"name"
bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]

print(bios_new.head())
print(bios_new.query('first_name == "Keith"'))

print(bios_new.info())


# here we adding the new column as "born_datetime" and adding his copy like"born_date"
bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'])



##CONVERTING THE TYPES LIKE FROM DATE TO YEARS
bios_new['born_year'] = bios_new['born_datetime'].dt.year

print(bios_new[['name','born_year']])