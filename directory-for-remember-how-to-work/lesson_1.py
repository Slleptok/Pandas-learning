import pandas as pd




'''
# initializing dataframe
# pritn all matrix
# print all columns from matrix
# print all index from matrix
# print full info about matrix include(rows,columns,dtype,size...)
# print description about matrix
# print nunique print a dtype and short descript
# print shape of matrix
'''
# initializing dataframe
dframe = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]] , columns=['A','B','C'], index=['1','2','3'])

# pritn all matrix
print(df.head())
print(dframe.head())

# print all columns from matrix
print(df.columns)
print(dframe.columns)

# print all index from matrix
print(df.index)
print(dframe.index)

# print full info about matrix include(rows,columns,dtype,size...)
print(df.info)
print(dframe.info)

# print description about matrix
print(df.describe())
print(dframe.describe())

# print nunique print a dtype and short descript
print(dframe.nunique())
print(df.nunique())\

# print shape of matrix
print(df.shape)
print(dframe.shape)