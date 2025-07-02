import pandas as pd

#LOAD THE DATA
df=pd.read_csv("Sales_Profit_Analysis.csv")

#VIEW TOP ROWS
print(df.head())

#CHECK FOR MISSING DATA
print(df.isnull().sum())

#CONVERT DATE COLUMN
df['Date']=pd.to_datetime(df['Date'])

#ADD NEW COLUMN : PROFIT / LOSS
df['Profit Status']=df['Profit'].apply(lambda x:'Profit'if x>0 else 'Loss')
print(df)

#SAVED CLEANED DATA
df.to_csv("clean_data.csv",index=False)