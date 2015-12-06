import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('pts.csv')

groupby_set= df.groupby('set') 
df1= groupby_set.sum()


df1.to_csv('linearregression.csv')
#to draw figure 
figure = plt.figure()
plt.plot(groupby_set.sum())
plt.show()