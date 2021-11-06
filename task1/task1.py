import pandas as pd
import re

df1=pd.read_csv("dataset1.csv",dtype={'name': str, 'price': float}) #Remove any zeros prepended to the price field; float type won't contain leading zeros
df2=pd.read_csv("dataset2.csv")

#Delete any rows which do not have a name, this also solve the dirty data issues
df1 = df1[~df1["name"].isnull()]
df2 = df2[~df2["name"].isnull()]

#Remove any zeros prepended to the price field; float type won't contain leading zeros
df2['price']=df2['price'].astype(float)

#concating both df into single df
df_full = pd.concat([df1,df2], ignore_index=True)


#Split the name field into first_name, and last_name
"""
Given no structure information about the name, I briefly browse through the name field:
Assumption made:
1. First Name & Last Name is a must
2. Prefix may be put, and always ends with "." except "Miss"
3. Suffix may be put
4. No middle name is ever provided
"""