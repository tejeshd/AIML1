import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])
print("sum of array = ",a.sum())
print("maximum of array = ",a.max())
print("minimum of array = ",a.min())
print("maximum of array = ",a.max(axis=1))
print("minimum of array = ",a.min(axis=1))
print("cumilative sum  of array = ",a.cumsum(axis=1))
print("cumilative sum of array = ",a.cumsum())
print("average  of array = ",a.mean())
print("transpose of array = ",a.transpose())
print("sum of array = ",a+b)

