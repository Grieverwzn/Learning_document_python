import pandas as pd
import numpy as np

df1=pd.DataFrame({'key':['X','Y','Z'],'data_set_1':[1,2,3]})
df2=pd.DataFrame({'key':['X','Y','C','X'],'data_set_2':[5,4,6,6]})

print(pd.merge(df1,df2))
print(pd.merge(df1,df2,on='key',how='inner'))
print(pd.merge(df1,df2,on='key',how='left'))
print(pd.merge(df1,df2,on='key',how='right'))
print(pd.merge(df1,df2,on='key',how='outer'))