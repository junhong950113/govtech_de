import pandas as pd

df1=pd.read_csv("dataset1.csv",dtype={'name': str, 'price': float}) #Remove any zeros prepended to the price field; float type won't contain leading zeros
df2=pd.read_csv("dataset2.csv")

#Delete any rows which do not have a name, this also solve the dirty data issues
df1 = df1[~df1["name"].isnull()]
df2 = df2[~df2["name"].isnull()]

#Remove any zeros prepended to the price field; float type won't contain leading zeros
df2['price']=df2['price'].astype(float)

