import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("clean_data.csv")
df['Date']=pd.to_datetime(df['Date'])

#SALES BY CITY
city_sales=df.groupby('City')['Sales'].sum().sort_values()
city_sales.plot(kind='barh',title='SALES BY CITY', color='skyblue')
plt.xlabel('Total Sales')
plt.tight_layout()
plt.show()

#PROFIT BY CATEGORY
sns.barplot(x='Category',y='Profit', data=df , estimator=sum)
plt.title('Total Profit By Category')
plt.show()

#TOP 5 PRODUCTS BY SALES
top_products=df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
top_products.plot(kind='bar', title='Top 5 Products By Sales')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("clean_data.csv")
df['Date']=pd.to_datetime(df['Date'])

#SALES BY CITY
city_sales=df.groupby('City')['Sales'].sum().sort_values()
city_sales.plot(kind='barh',title='SALES BY CITY', color='skyblue')
plt.xlabel('Total Sales')
plt.tight_layout()
plt.show()

#PROFIT BY CATEGORY
sns.boxplot(x='Category',y='Profit', data=df , estimator=sum)
plt.title('Total Profit By Category')
plt.show()