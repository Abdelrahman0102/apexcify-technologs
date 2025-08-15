import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sales_data.csv")
print(df.head(12))
df.index=range(1,len(df)+1)
print(df)
plt.plot(df["Sales"],marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()

