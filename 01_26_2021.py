# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:34:37 2021

@author: HeSer
"""
#%% Load packages 
# add as many comments as you can 

import numpy as np 
import pandas as pd 
# x = 2 
# print(x)

# %%It is always a good idea to start simple 

df = pd.read_csv("C:/Users/HeSer/OneDrive/Documents/Wharton/Wharton Spring 2021/FNCE737/FNCE737/Data/NKLA.csv")
print(df.head(6))
# ticker = "NKLA"

# tt2= pd.read_csv("C:/Users/HeSer/OneDrive/Documents/Wharton/Wharton Spring 2021/FNCE737/FNCE737/Data/"+ ticker+".csv")
#%%
df.head(6)
#%% explore the data

# df.head(10)
#%%

# df.tail(6)
#%%

#df.columns()

#%%
# df.describe()
#%%
# df.dtypes()
#%%
df.info()
#%%

print(df.sort_values("users_holding"))
# df.sort_values("user_holding", "timestamp")
#%%
df["datetime"]= pd.to_datetime(df["timestamp"])
print(df.head(6))
#%%
df["date"] = df["datetime"].dt.date
#%%
df_daily = df.groupby("date").agg({"users_holding": "mean"})
print(df_daily.head(6))
#%%
df_daily.index = pd.to_datetime(df_daily.index)
#%%
print(df_daily["2020"].head(20))
# print("Hello")
#%% get price and volume data from yahoo finance
import yfinance as yf
#%%
tickers = "NKLA"
start_date = df_daily.index.min()
end_date = df_daily.index.max()
freq = "id"
p_df = yf.download(tickers, start=start_date, end=end_date)

#%%
print(p_df.head(6))
#%%
p_df.head(20)
#%%

#%%

#%%
#%%
#%%
#%%
#%%
#%%
#%%

