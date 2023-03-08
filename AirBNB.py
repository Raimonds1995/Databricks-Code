# Databricks notebook source
import pandas as pd
import numpy as nap
import seaborn as sns
from matplotlib import pyplot as plt
from pandas_profiling import ProfileReport

#!pip install pandas-profiling
#dbutils.library.restartPython()

airbnb = pd.read_csv("/dbfs/FileStore/NetflixData/amsterdam_weekdays.csv")


# COMMAND ----------

airbnb.head()
#airbnb.columns
airbnb.count()
airbnb.info()

# COMMAND ----------

airbnb = ProfileReport(airbnb)

airbnb

# COMMAND ----------

airbnb = airbnb.dropna(subset=['bedrooms'])
#airbnb = airbnb[airbnb['bedrooms'].notna()]
#airbnb_copy['bedrooms'] = airbnb_copy['bedrooms'].astype(int)
#airbnb_copy['realSum'] = airbnb_copy['realSum'].astype()
#airbnb_copy.head(1-10)
airbnb.count()

# COMMAND ----------

sns.countplot(x=airbnb_copy['room_type'], orient='v')
plt.xticks(rotation=90)
plt.xlabel('Type of rooms')
plt.show()

# COMMAND ----------

sns.countplot(x=airbnb_copy['bedrooms'])
plt.xlabel('Number of Bedrooms')
plt.title("Number of Airbnb with available amount of bedrooms")
plt.ylabel("Number of AirBnb's")
plt.show()

# COMMAND ----------

sns.countplot(x=airbnb_copy['cleanliness_rating'], orient='v')
plt.show()

# COMMAND ----------

#airbnb_copy['bedrooms'].unique()
y = airbnb_copy[['bedrooms']]

y.isnull().sum()

# COMMAND ----------

airbnb_copy.groupby(['room_type']).mean().plot.bar(y= "guest_satisfaction_overall")
plt.xticks(rotation=0)
plt.ylabel("Guest Satisfaction Score from 0-100")
plt.title('Graph showing average guest satisfaction score for each room type')
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100])
plt.axhline(airbnb_copy.guest_satisfaction_overall.mean(), linestyle= '--', color='red')
plt.show()

# COMMAND ----------

airbnb_copy.groupby(['room_type']).mean().plot.bar(y= "bedrooms")
plt.show()

# COMMAND ----------

airbnb_copy.groupby(['bedrooms']).mean().sort_values(by = 'realSum').plot.bar(y='realSum', label='Average Price Data')
plt.legend(loc= 'upper left')
plt.xticks(rotation=0)
plt.title("Graph showing average price of AirBnb based on bedrooms")
plt.xlabel('Amount of Bedrooms')
plt.ylabel('Average Price')
plt.show()


# COMMAND ----------

airbnb_copy = airbnb_copy.groupby(['room_type']).mean()
airbnb_copy = airbnb_copy.reset_index()
airbnb_copy= realSum.sort_values('realSum'),ascending=[0])
airbnb_copy.head()

# COMMAND ----------


