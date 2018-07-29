import pandas as pd

link_df=pd.read_csv('input_link.csv',encoding='gbk')
link_df=link_df.dropna(axis=1)
link_df1=link_df.sort_values('from_node_id')
print(link_df1)



# print(link_df.describe())
# print(link_df.sum(axis=1))
# print(link_df.min(axis=1))
#
# s1=pd.Series(np.random.rand(10))
# print(s1.sort_values(ascending=False))
# print(s1.sort_values())
# print(s1.sort_values().sort_index(ascending=False))