import pandas as pd
import numpy as np

def test_map_1(x):
    return x+1
def test_map_2(x):
    return x+'_ABC'

df1=pd.DataFrame(np.arange(9).reshape(3,3),index=['BJ','SH','GZ'],columns=['a','b','c'])
df1.index=df1.index.map(str.lower)
print(df1)
df1=df1.rename(index=str.upper)
print(df1)
df1=df1.rename(index={'BJ':'Beijing'})
print(df1)

list1=[1,2,3]
# learn to use map function instead of other methods
print(list(map(test_map_1,list1)))
df1.index=df1.index.map(test_map_2)
print(df1)
df1=df1.rename(index=test_map_2,columns=test_map_2)
print(df1)

