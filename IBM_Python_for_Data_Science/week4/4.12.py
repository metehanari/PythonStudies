#pandas working.save data

import pandas as pd

data = {"Release":["1982","1980","1977","1980","1981","1977","1982"]}
# this is a dictionary

df = pd.DataFrame(data)
# this is a dataframe

df["Release"].unique()
# unique values in the column