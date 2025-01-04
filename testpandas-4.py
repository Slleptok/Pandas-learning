import pandas as pd

coffee = pd.read_csv("./warmup-data/coffee.csv")
print(coffee.head())


### loc & iloc

## loc
print(coffee.loc[0])

# loc for tables
print(coffee.loc[[0,1,2]])      

# loc from 5 to 8 like 5:8
print(coffee.loc[5:8])

#get some columns like "Days" , "Units Sold" etc
print(coffee.loc[5:8, "Day"])
print(coffee.loc[5:8, ["Day" , "Units Sold"]])



## iloc

coffee.index = coffee["Day"] # -> when you state the personal index by horizontal in columns

print(coffee.iloc[0:5,[0,2]])





### seting data frame value
coffee.loc[1,"Units Sold"] = 10
print(coffee)
