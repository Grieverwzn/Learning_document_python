import numpy as np
import pandas as pd

def add(x):
    return x+1


link_df = pd.read_csv('input_link.csv',encoding='gbk')
link_df=link_df.dropna(axis=1)
link_df['link_id']=link_df['link_id'].apply(add)
link_df['name']=link_df['name'].apply(str.upper)
#print(link_df.head())

def foo(line):
    l1=line.strip().split(',')
    #print(l1[2])
    return pd.Series([l1[1],l1[2]])

df_tmp=link_df['geometry'].apply(foo)
df_tmp=df_tmp.rename(columns={0:'latitude',1:'magtude'})
print(df_tmp)
link_df=link_df.combine_first(df_tmp)
link_df.to_csv('input_link_2.csv')
