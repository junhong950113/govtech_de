import pandas as pd

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

#defining a function to transform name field
def name_transformation(x):
    i = x.split(" ")
    if len(i) == 2: # length of 2 must be first name & last name
        return i[0] + " " + i[1];
    elif len(i) == 4: # length of 4 must be prefix & first name & last name & suffix
        return i[1] + " " + i[2];
    elif len(i) == 3: # length of 3 must be prefix & first name & last name OR first name & last name & suffix
        if (i[0].find(".") >= 0) or (i[0].find("Miss") >= 0):  #prefix & first name & last name
            return i[1] + " " + i[2];
        else: #first name & last name & suffix
            return i[0] + " " + i[1];

df_full['name'] = df_full['name'].apply(name_transformation) #applying the transformation

#splitting into first_name & last_name field
df_name_full = df_full['name'].str.split(expand=True)
df_full["first_name"] = df_name_full[0]
df_full["last_name"] = df_name_full[1]

#Create a new field named above_100, which is true if the price is strictly greater than 100
df_full["above_100"] = df_full['price']>100

#final csv
df_final = df_full[["first_name","last_name","price","above_100"]]

df_final.to_csv("final_output.csv", index=False)