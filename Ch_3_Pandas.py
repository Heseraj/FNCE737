#%% This is for practice in chapter 3, pandss

import numpy as np
import pandas as pd

# talking about Vix, volatility index for s&p500
#%%
df1 = pd.read_csv("Data/NKLA.csv")

#%%
# print(df1.head(10))

# print(df1.tail(2))

print(df1.columns())
