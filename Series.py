import numpy as np
import pandas as pd

series_1 =pd.Series([1,2,34])
print(series_1)
print(series_1.values)

series_2=pd.Series(np.arange(10))
series_3=pd.Series({1:1,2:2,3:3})
print(series_2)
print(series_3)
print(series_3.values)
print(series_3.index)

series_4 =pd.Series([1,2,3,4],index=['A','B','C','D'],dtype='object')
print(series_4)
print(series_4['B'])
print(series_4>=3)

series_4=series_4.to_dict()
print(series_4)
series_5=pd.Series(series_4)
print(series_5)
index_1=['A','B','C','D','E']
series_6=pd.Series(series_5,index=index_1)
print(series_6)
print(pd.isnull(series_6))
print(pd.notnull(series_6))
series_6.name='demo'
print(series_6)
series_6.index.name='index_name'
print(series_6.index)
