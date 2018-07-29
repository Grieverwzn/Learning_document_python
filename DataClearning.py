import numpy as np
import pandas as pd


link_df=pd.read_csv('input_link.csv',encoding='gbk')
link_df=link_df.dropna(axis=1)
print(link_df.head())
print(link_df['number_of_lanes'].unique())
print(link_df['number_of_lanes'].duplicated())
print(link_df['number_of_lanes'].drop_duplicates(keep='last'))
print(link_df['number_of_lanes'].drop_duplicates(keep='first'))