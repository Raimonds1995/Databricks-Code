# Databricks notebook source
import pandas as pd

# COMMAND ----------

pd.DataFrame({'Yes' : [50, 21], 'No' : [131 ,2]})

# COMMAND ----------

pd.DataFrame({'Bob' : ['I liked it.', 'It was awful'] ,
              'Sue' : ['Pretty Good.', 'Bland']},
             index =['Prodcut A', 'Product B'])

# COMMAND ----------

pd.Series([1,2,3,4,5])

# COMMAND ----------

pd.Series([30,40,50], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# COMMAND ----------

wine_review= pd.read_csv('https://raw.githubusercontent.com/Raimonds1995/Databricks-Code/main/winemag-data-130k-v2.csv')

print(wine_review)

# COMMAND ----------

wine_review.country

wine_review['country'][0:5]


# COMMAND ----------

wine_review.iloc[:10,0]

# COMMAND ----------

wine_review.iloc[1:10, 1]

# COMMAND ----------

wine_review.iloc[5:]

# COMMAND ----------

wine_review.loc[0:10,['country', 'price', 'taster_name']]

# COMMAND ----------

wine_review.loc[(wine_review.country == 'Italy') | (wine_review.points >=90)]

# COMMAND ----------

wine_review.loc[wine_review.country.isin(['Italy', 'France'])]

# COMMAND ----------

wine_review.points.describe()

# COMMAND ----------

wine_review.taster_name.value_counts()

# COMMAND ----------

wine_review.head(1)

# COMMAND ----------

wine_review.head(5)

# COMMAND ----------

wine_review.country + " - " + wine_review.region_1

# COMMAND ----------

wine_review.groupby('points').price.min()

# COMMAND ----------

wine_review.groupby('winery').apply(lambda df: df.title.iloc(0))

# COMMAND ----------

wine_review.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

# COMMAND ----------

wine_review.groupby(['country']).price.agg([len, min, max])

# COMMAND ----------

wine_review = wine_review.reset_index()
wine_review.sort_values(by= 'price')

# COMMAND ----------

wine_review.sort_values(by='price', ascending=False)

# COMMAND ----------

wine_review.dtypes

# COMMAND ----------

wine_review.points.astype('float64')

# COMMAND ----------

wine_review[pd.isnull(wine_review.country)]

# COMMAND ----------

wine_review.taster_twitter_handle.replace("@kerinokeefe", "kerino")

# COMMAND ----------

wine_review.rename(index={0: 'firstEntry', 1:'secondyEntry'})

# COMMAND ----------

wine_review.rename(columns={'points' : 'price'})

# COMMAND ----------


