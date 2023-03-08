# Databricks notebook source
import pandas as pd
import numpy as np
import seaborn as sns

#!pip install openpyxl
#dbutils.library.restartPython()

sns.set_style('whitegrid')

raw_df = pd.read_excel("/dbfs/FileStore/NetflixData/2018_Sales_Total_v2.xlsx")
df = raw_df.groupby(['account number', 'name'])['ext price'].sum().reset_index()
df.head()
df['ext price'].plot(kind='hist')
df['ext price'].describe()
pd.qcut(df['ext price'], q=4)
df['quantile_ex_1'] = pd.qcut(df['ext price'], q=4)
df['quantile_ex_2'] = pd.qcut(df['ext price'], q=10, precision=0)
df.head()


# COMMAND ----------

df['quantile_ex_1'].value_counts()

# COMMAND ----------

df['quantile_ex_2'].value_counts()

# COMMAND ----------

bin_labels_5 = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond']
df['quantile_ex_3'] = pd.qcut(df['ext price'],
                              q=[0, .2, .4, .6, .8, 1],
                              labels=bin_labels_5)
df.head()

# COMMAND ----------

df['quantile_ex_3'].value_counts()

# COMMAND ----------

results, bin_edges = pd.qcut(df['ext price'],
                             q=[0, .2, .4, .6, .8, 1],
                             labels=bin_labels_5,
                             retbins=True)
results_table = pd.DataFrame(zip(bin_edges, bin_labels_5),
                            columns=['Threshold', 'Tier'])
results_table

# COMMAND ----------

df.describe(include='category')

# COMMAND ----------

df.describe(percentiles=[0, 1/3, 2/3, 1])

# COMMAND ----------

df['quantile_ex_4'] = pd.qcut(df['ext price'],
                             q=[0, .2, .4, .6, .8, 1],
                             labels=False)
df.head()

# COMMAND ----------

df = df.drop(columns = ['quantile_ex_1', 'quantile_ex_2', 'quantile_ex_3', 'quantile_ex_4'])
pd.cut(df['ext price'], bins=4)

# COMMAND ----------

pd.cut(df['ext price'], bins=4).value_counts()

# COMMAND ----------

cut_labels_4 = ['silver', 'gold', 'platinum', 'diamond']
cut_bins = [0, 70000, 100000, 130000, 200000]
df['cut_ex1'] = pd.cut(df['ext price'], bins=cut_bins, labels=cut_labels_4)
df.head()

# COMMAND ----------

np.linspace(0, 200000, 9)

# COMMAND ----------

pd.cut(df['ext price'], bins=np.linspace(0, 200000, 9))

# COMMAND ----------

np.arange(0, 200000, 10000)

# COMMAND ----------

pd.interval_range(start=0, freq=10000, end=200000, closed='left')

# COMMAND ----------

interval_range = pd.interval_range(start=0, freq=10000, end=200000)
df['cut_ex2'] = pd.cut(df['ext price'], bins=interval_range, labels=[1,2,3])
df.head()

# COMMAND ----------

df['ext price'].value_counts(bins=4, sort=False)

# COMMAND ----------

############ Task 2 Below ########


# COMMAND ----------

from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

#define input string
data = 'hello world'
print(data)
# define universe of possible input value
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# define a mapping of chars to integers
chart_to_int = dict((c, i) for i, c in enumerate(alphabet))
int_to_char = dict((i, c) for i, c in enumerate(alphabet))
# integer encode input data
integer_encoded = [chart_to_int[char] for char in data]
#print(integer_encoded)
# one got encode
onehot_encoded = list()
for value in integer_encoded:
    letter = [0 for _ in range(len(alphabet))]
    letter[value] = 1
    onehot_encoded.append(letter)
print(onehot_encoded)
# invert encoding
inverted = int_to_char[argmax(onehot_encoded[0])]
print(inverted)

# COMMAND ----------

from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# define example
data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
value = array(data)
print(values)
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print(integer_encoded)
# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded  = integer_encoded.reshape(len(integer_encoded),1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
# invert first example
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0,:])])
print(inverted
     )


# COMMAND ----------

from keras.utils import to_categorical

# define example
data = [1,3,2,0,3,2,2,1,0,1]
data = array(data)
print(data)
# one hot encode
encoded = to_categorical(data)
print(encoded)
# invert encoding
inverted = argmax(encoded[0])
print(inverted)


# COMMAND ----------


