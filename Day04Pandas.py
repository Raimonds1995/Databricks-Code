# Databricks notebook source
list1 = [1,2,3,4,5]
list2 = [[1,2,3,4],[4,5,6,7,8]]

# [1,2,3]
# [4,5,7]
# [8,9,10]

print(list1[1])

# COMMAND ----------

import pandas as pd




# COMMAND ----------

#dict1 = {'key' : 'value' , 'word1' : 'definition1', 'value1' :12}
#print(dict1['key'])


df = pd.DataFrame({
    'a' : [1,2,3],
    'b' : [4,5,6],
    'c' : [7,8,9],
}, index = [1,2,3])


df2 = pd.DataFrame(
    [[1,2,3],[4,5,6],[7,8,9]],
    index=[1,2,3],
    columns = ['a', 'b', 'c'])
print(df)
print("break")
print(df2)


# COMMAND ----------

print(df)

# COMMAND ----------

tipsData = pd.read_csv(windemag-data-130k-vs.csv)

print(tipsData.head(5))
print(tipsData.describe())

print(tipsData.isnull().sum())




# COMMAND ----------

tipsData.groupby(['day']).count()



# COMMAND ----------

tipsData.groupby(['day']).sum()

# COMMAND ----------

totalTips = tipsData.groupby(['day']).sum()['tip']
totalBill = tipsData.groupby(['day']).sum()['total_bill']

tipDayPercentage = (100 * totalTips / totalBill)

tipDayPercentage = tipDayPercentage.to_frame('tip(%)').reset_index()

print(tipDayPercentage)

# COMMAND ----------


