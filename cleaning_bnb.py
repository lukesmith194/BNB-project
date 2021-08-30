import pandas as pd
import numpy as np
import re

dfbnb = pd.read_csv("data/bnb.csv")
dfbnb["Daily_diff($)"] = dfbnb.High - dfbnb.Low
dfbnb.drop(["Open"] ,axis= 1, inplace= True)
dfbnb1 = dfbnb.rename(columns={"Price(in dollars)": "Price($,mean)"})
dfbnb2= dfbnb1[["Date", "Price($,mean)", "High", "Low", "Daily_diff($)","Change%","Vol."]]
dfbnb2['Date']=pd.to_datetime(dfbnb2['Date'], infer_datetime_format='%Y-%m-%d')
hola = dfbnb2.iloc[::-1]
hola.reset_index(drop = True,inplace=True)
dfbnb3 = hola
print(dfbnb3)