import pandas as pd




'''
# using output parametrs like  .head() .tail() .sample()
# loc & iloc
# loc
# loc for geting personal data
# loc for geting data in period
# also use loc to get a personal solumns
# iloc
# Get the element at row 2 and column 3
# Get rows
# Get columns
# Get data rows in period Slice Rows
# Get data columns in period Slice Columns
# Get specific rows (0, 2) and columns (0,2)
# Get rows 1 and 3 with all columns
# Get rows 0 to 3 and columns 1 and 3
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

# Modify a specific element
coffee.loc['2', 'Day'] = 50
print(coffee.head())

# loc for geting data in period
print(coffee.loc[5:8])
print(coffee.loc[1:5])
print(coffee.loc[4:9])
print(coffee.loc[:]) # empty indetificator get all values

# also use loc to get a personal columns
print(coffee.loc[5:8], "Day")
print(coffee.loc[:,['Day','Units Sold']])
print(coffee.loc[:, ['Day','Units Sold', 'Coffee Type']])

# Update rows based on a condition


# iloc
# Get the element at row 2 and column 3
# Architecture df.iloc[row_selection, column_selection]
print(coffee.iloc[0,1])
print(coffee.iloc[3,1])

# Get rows
print(coffee.iloc[3])
print(coffee.iloc[6])
print(coffee.iloc[0])

# Get columns
print(coffee.iloc[:,0])
print(coffee.iloc[:,1])
print(coffee.iloc[:,2])

# Get data rows in period Slice Rows
print(coffee.iloc[1:4])

# Get data columns in period Slice Columns
print(coffee.iloc[:, 1:3])

# Get specific rows (0, 2) and columns (0,2)
print(coffee.iloc[[0, 2], [0, 2]])

# Get rows 1 and 3 with all columns
print(coffee.iloc[[1, 3], :])

# Set the element at row 2, column 3 to 99
coffee.iloc[1, 2] = 99
print(coffee.head())

# Get rows 0 to 3 and columns 1 and 3
print(coffee.iloc[0:3, [0, 2]])



## loc: Uses label-based indexing
## iloc: Uses integer-based indexing.