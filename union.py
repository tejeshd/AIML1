import pandas as pd
import numpy as np
ser1=pd.Series([10,20,30])
ser2=pd.Series([1,2,3,4,5])
u=pd.Series(np.union1d(ser1,ser2))
i=pd.Series(np.intersect1d(ser1,ser2))
notcommon=u[~u.isin (i)]
print(u)
print(i)
