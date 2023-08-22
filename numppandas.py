import pandas as pd
import numpy as np
num=np.array([10,20,30,40])
s=pd.Series(num)
print(s)

s=pd.Index([10,20,30,40])
print(s.value_counts())
