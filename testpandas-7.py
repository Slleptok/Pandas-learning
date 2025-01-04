import pandas as pd


bios = pd.read_csv('./data/bios.csv')
coffee = pd.read_csv("./warmup-data/coffee.csv")

#bios_new = bios.copy()


###ADDING AND REMOVING COLUMNS USING LAMDA
"""
# If height_cm contains the values [160, 170, 180, 190, 155], 
# the new column height_category
# will contain [Short, Average, Average, Tall, Short]
"""
bios['height_category'] = bios['height_cm'].apply(lambda x: 'Short' if x < 165 else ('Average' if x < 185 else 'Tall'))
print(bios.head())



"""
# Categorize athletes into Lightweight, Middleweight,
# or Heavyweight based on height and weight.
"""
def categorize_athlete(row):
     if row['height_cm'] < 175 and row['weight_kg'] < 70:
         return 'Lightweight'
     elif row['height_cm'] < 185 or row['weight_kg'] <= 80:
         return 'Middleweight'
     else:
         return 'Heavyweight'

bios['Category'] = bios.apply(categorize_athlete, axis = 1)
print(bios.head())



###MERGING AND CONCATENATING DATA

nocs = pd.read_csv('./data/noc_regions.csv')
print(nocs.head())

bios_new =pd.merge(bios,nocs,left_on = 'born_country', right_on='NOC', how='left')
print(bios_new)
bios_new.rename(columns={'region':'born_country_full'},inplace=True)
print(bios.head())

bios_new[bios_new['NOC_x'] != bios_new['born_country_full']][['name','NOC_x','born_country_full']]
print(bios_new[bios_new['born_country'] == 'USA'])
