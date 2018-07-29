import numpy as np
import pandas as pd

DICT=dict({'City':['Beijing','Shanghai','Guangzhou'],'Pop':['3000','2000','1500']})
df1=pd.DataFrame(DICT)
print(df1)

#df1['GDP']=pd.Series([2000,2000,1000,])
gdp_map={'Beijing':2000,'Shanghai':2000,'Guangzhou':1500}
df1['GDP']=df1['City'].map(gdp_map)
print(df1)

s1=pd.Series(np.arange(10))
print(s1.replace([1,2,3],[100,200,np.nan]))