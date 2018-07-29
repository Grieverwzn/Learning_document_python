import pandas as pd
import numpy as np

link_df = pd.read_csv('input_link.csv',encoding='gbk')
print(link_df.head(2))
print(link_df['name'])
print(link_df[['name','jam_density']])
print(link_df['name'][1])
sub_link_df=link_df[['name','jam_density']]
print(sub_link_df)

# 区分Iloc 与loc
xx1=sub_link_df.iloc[10:20,0:2]
print(xx1)
xx2=sub_link_df.loc[10:20,'jam_density']
print(xx2)

s1=pd.Series([1,2,3,4],index=['A','B','C','D'])
print(s1)
s2=s1.reindex(['A','B','C','D','E'])
print(s2)
s3=s1.reindex(['A','B','C','D','E'],fill_value=10)
print(s3)
s4=pd.Series(['A','B','C'],index=[1,10,20])
print(s4)
s5=s4.reindex(range(20))
print(s5)
s6=s4.reindex(range(20),method='ffill')
print(s6)

df1=pd.DataFrame(np.random.rand(25).reshape([5,5]),index=['A','B','D','E','F'],columns=['c1','c2','c3','c4','c5'])
print(df1)
df1=df1.reindex(index=['A','B','C','D','E','F'],columns=['c1','c2','c3','c4','c5','c6'])
print(df1)
print(df1.drop('A'))
print(df1.drop('c1',axis=1))

N=np.nan
print(N)
print(type(N))

series_1=pd.Series([N,3,4],index=['A','B','C'])
print(series_1)
print(series_1.isnull())
print(series_1.notnull())
print(series_1.dropna())
