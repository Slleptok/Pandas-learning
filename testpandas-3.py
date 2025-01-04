import pandas as pd

coffee = pd.read_csv("./warmup-data/coffee.csv")
print(coffee.head())

# for what we using like  .head() .tail() .sample()

#.head - data from top
print(coffee.head())
print(coffee.head(10))
print(coffee.head(5))

#.tail - data from bottom
print(coffee.tail())
print(coffee.tail(10))
print(coffee.tail(5))

#.sample - give some random data
print(coffee.sample())
print(coffee.sample(10))
print(coffee.sample(5))
