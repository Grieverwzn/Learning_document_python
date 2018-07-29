import numpy as np
import pandas as pd



link_df=pd.read_csv('input_link.csv',encoding='gbk')
print(link_df.dropna(axis=1,how='all',thresh=2))
#'all'所有为Nan删除，any 有一个删除,thresh超过2各
print(link_df.fillna(value=0))

