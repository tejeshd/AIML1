import pandas as pd
data = pd.read_csv("C:/Users/SPTINT-10/Desktop/tejesh/Iris (1).csv")
print(data)
print(data.tail(10))
print(data.head(5))
print(data["PetalWidthCm"])
print(data.describe())
print(data.info())
print(data.dtypes)
print(data.count())

