import pandas as pd
import numpy as np

s1=pd.Series(np.random.rand(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])
#print(s1)
#print(s1[1])
print(s1[1]['a'])
print(s1[:,'a'])
print(s1.unstack())
print(s1.unstack().T)
print(s1.unstack().T.unstack())

df1=pd.DataFrame(np.arange(16).reshape(4,4),index=[['a','a','b','b'],[1,2,1,2]],columns=[['BJ','SH','GZ','GZ'],[1,2,3,3]])
#print(df1)
#print(df1['GZ'])
print(df1.loc['a']['BJ'][1][1])


