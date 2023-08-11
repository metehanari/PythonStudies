#dataframe

import pandas as pd

path = "C:\\Users\\HP\\Desktop\\csv1.csv" #path of the file

df = pd.read_csv(path) #read the csv file

x = df[["Country"]] #print the column named "Country"

print(x) 

print(df.iloc[0]) #print the first row of the dataframe