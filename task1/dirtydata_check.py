"""
Spot dirty data when writing these code:
df2=pd.read_csv("dataset2.csv",dtype={'name': str, 'price': float})

realized that in dataset2.csv, it containing values of column 'name'

checking for both file to spot if any other dirty data exists
"""

import pandas as pd
import re

df1=pd.read_csv("dataset1.csv")
df2=pd.read_csv("dataset2.csv")


#to check whether col 'name' in dataset1 contain any price values
df1_name=df1['name'].tolist()
df1_name_wrong={}
for i in df1_name:
    x=re.findall("[0-9]",str(i))
    if len(x)>0:
        key1=df1_name.index(i)
        df1_name_wrong[key1]=i
print("df1_name_wrong:", df1_name_wrong)


#to check whether col 'price' in dataset1 contain any name values
df1_price=df1['price'].tolist()
df1_price_wrong={}
for i in df1_price:
    x=re.findall("[^0-9.]",str(i))
    if len(x)>0:
        key1=df1_price.index(i)
        df1_price_wrong[key1]=i
print("df1_price_wrong:", df1_price_wrong)


#to check whether col 'name' in dataset2 contain any price values
df2_name=df2['name'].tolist()
df2_name_wrong={}
for i in df2_name:
    x=re.findall("[0-9]",str(i))
    if len(x)>0:
        key1=df2_name.index(i)
        df2_name_wrong[key1]=i
print("df2_name_wrong:", df2_name_wrong)


#to check whether col 'price' in dataset2 contain any name values
df2_price=df2['price'].tolist()
df2_price_wrong={}
for i in df2_price:
    x=re.findall("[^0-9.]",str(i))
    if len(x)>0:
        key1=df2_price.index(i)
        df2_price_wrong[key1]=i
print("df2_price_wrong:", df2_price_wrong)

"""
Output of this python script showing that dirty data in dataset2 col 'price':
name values exists in dataset2 col 'price'
"""