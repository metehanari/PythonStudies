#pandas working.save data

import pandas as pd

data = {"Release":["1982","1980","1977","1980","1981","1977","1982"]}

df = pd.DataFrame(data)

df_csv = df.to_csv("week4\df.csv")