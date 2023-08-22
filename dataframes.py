import pandas as pd
data={'day':[0,1,2,3,4,5,6,7,8,9],
      'steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7619]}
df=pd.DataFrame(data)
df['steps']=df['steps']+1000
print(df)

data={'day':[0,1,2,3,4,5,6,7,8,9],
      'steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7619]}
fs=pd.DataFrame(data)
print(fs)
 
print(fs.loc[fs['steps']>7000])
