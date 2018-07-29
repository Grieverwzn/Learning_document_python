import pandas as pd
import numpy as np
from _datetime import datetime

t1=datetime(2009,10,3)
t2=datetime(2007,6,20)
t3=datetime(2012,12,12)
t4=datetime(2013,2,10)
t5=datetime(2012,1,23)
datelist=[t1,t2,t3,t4,t5]

s1=pd.Series(np.random.rand(5),index=datelist)
s1=s1.sort_values(ascending=True)
print(s1)


