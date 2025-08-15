import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sales_data.csv")
print(df.head(12))
df.index=range(1,len(df)+1)
print(df)
df.plot()
plt.show()
