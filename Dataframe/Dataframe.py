import numpy as np
import pandas as pd
#import webbrowser

#link='http://pandas.pydata.org/pandas-docs/version/0.20/io.html'
#webbrowser.open(link)

df1=pd.read_clipboard() # 获取剪贴板上的讯息
df1.to_csv('df1.csv')
df1.to_csv('df1_1.csv',index=False)
#print(df1)
print(df1.head())
df2=pd.read_csv('df1_1.csv')
df2.to_excel('df2.xlsx')
print(df2)
df2.to_html('df2.html')


#print(df1[0:1])



