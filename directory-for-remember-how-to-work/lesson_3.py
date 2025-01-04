import pandas as pd




'''
# using output parametrs like  .head() .tail() .sample()
# loc & iloc
# loc
# loc for geting personal data
# loc for geting data in period
# also use loc to get a personal solumns
# iloc
'''

coffee = pd.read_csv('../warmup-data/coffee.csv')

# using output parametrs like  .head() .tail() .sample()
# .head() - print data from top of matrix
print(coffee.head())
print(coffee.head(10))
print(coffee.head(5))

# .tail() - print data from anywere of matrix
print(coffee.tail())
print(coffee.tail(6))
print(coffee.tail(10))

# .sample() - print data from bottom of matrix
print(coffee.sample())
print(coffee.sample(5))
print(coffee.sample(13))


# loc & iloc
# loc
#  print(coffee.loc["index of ellement"])
print(coffee.loc[0])
print(coffee.loc[4])
print(coffee.loc[9])

# loc for geting personal data
print(coffee.loc[[0,1,2]])
print(coffee.loc[[0,2,4]])
print(coffee.loc[[1,3,5]])

# loc for geting data in period
print(coffee.loc[5:8])
print(coffee.loc[1:5])
print(coffee.loc[4:9])
print(coffee.loc[:]) # empty indetificator get all values

# also use loc to get a personal solumns
print(coffee.loc[5:8], "Day")
print(coffee.loc[:,['Day','Units Sold']])
print(coffee.loc[:, ['Day','Units Sold', 'Coffee Type']])



# iloc

coffee.index = coffee["Day"] # -> when you state the personal index by horizontal in columns
print(coffee.iloc[0:5,[0,2]])


# seting data frame value - or addding
coffee.loc[1,"Units Sold"] = 10
print(coffee[:])