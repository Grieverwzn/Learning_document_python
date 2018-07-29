import numpy as np
import pandas as pd

arr1=np.arange(9).reshape(3,3)
arr2=arr1
print(arr1)
print(np.concatenate([arr1,arr2]))
print(np.concatenate([arr1,arr2],axis=1))

s1=pd.Series([1,2,3],index=['x','y','z'])
s2=pd.Series([1,2],index=['A','B'])
print(pd.concat([s1,s2],axis=1))
print(pd.concat([s1,s2]))

df1=pd.DataFrame(np.random.rand(4,3),columns=['X','Y','Z'])
df2=pd.DataFrame(np.random.rand(3,3),columns=['X','Y','A'])

print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],axis=1))

s1=pd.Series([1,np.nan,3,np.nan],index=['A','B','C','D'])
s2=pd.Series([1,2,3,4],index=['A','B','C','D'])
print(s1.combine_first(s2))

