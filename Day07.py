# Databricks notebook source
import matplotlib.pyplot as plt
import numpy as np
import pyspark as ps
import pandas as pd

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv") #fine the csv. file location
profitList = df ['total_profit'].tolist()
monthList = df ['month_number'].tolist()
plt.plot(monthList, profitList, label='Profit data for last year',
         color='g', marker='o', markerfacecolor='k',
         linestyle='--', linewidth=3) #set parameters of graph, such as colour, linestyle, width etc
plt.xlabel('Month Number') # set x label
plt.ylabel('Total Profit') # sets y label
plt.title('Company profit per month') #set title for the graph
plt.legend(loc= 'lower right') #the label for line is located in bottom right
plt.show() #shows the graph

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv")
monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
shampooSalesData = df['shampoo'].tolist()
moisturizerSalesData = df['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData, label = 'Face Cream Sales Data', marker= 'o')
plt.plot(monthList, faceWashSalesData, label = 'Face Wash Sales Data', marker= 'o')
plt.plot(monthList, toothPasteSalesData, label = 'Tooth Paste Sales Data', marker= 'o')
plt.plot(monthList, bathingsoapSalesData , label = 'Bathing Soap Sales Data', marker= 'o')
plt.plot(monthList, shampooSalesData, label = ' Shampoo Sales Data', marker= 'o')
plt.plot(monthList, moisturizerSalesData, label = 'Moisturizer Sales Data', marker= 'o')

plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.title('Sales Data')
plt.legend(loc='upper left')
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.show()

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv")
monthList = df['month_number'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label='Tooth paste Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Numbers of units sold')
plt.title('Tooth paste Sales data')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.grid(True, linewidth=0.5, linestyle='--')
plt.show


# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv")
monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width=0.25, label='Face Cream Sales Data', align='edge' )
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width=-0.25, label='Face Wash Sales Data', align='edge' )


plt.title('Facewash and Facecream sales data')
plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.legend(loc='upper left')
plt.grid(True, linewidth=1, linestyle='--')
plt.xticks(monthList)
plt.show()

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv")
monthList = df['month_number'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()

plt.bar(monthList, bathingsoapSalesData)

plt.title('Bathingsoap Sales Date')
plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.grid(True, linewidth=1, linestyle='--')
plt.xticks(monthList)
plt.show()



# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv")
profitList= df['total_profit'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range= [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label='Profit data')
plt.legend(loc='upper left')
plt.xlabel('Profits range in dollar')
plt.ylabel('Actual profit in dollar')
plt.show()


# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv")
monthList = df['month_number'].tolist()

labels= ['Face Cream', 'Face Wash', 'Tooth Paste', 'Bathing Soap', 'Shampoo', 'Moisturizer']
salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]

plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.title('Sales Data')
plt.legend(loc='center left')
plt.show()
         

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv")
monthList = df['month_number'].tolist()
faceWashSalesData = df['facewash'].tolist()
bathingsoap = df['bathingsoap'].tolist()

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(monthList, bathingsoap, label='Bathingsoap Sales Data', color='g', marker='o', linewidth=1 )
axarr[0].set_title('Sales data of Bathingsoap')
axarr[1].plot(monthList, faceWashSalesData, label='Face Wash Sales Data', color='r', marker='o', linewidth=1)
axarr[1].set_title('Sales data of Facewash')

plt.xticks(monthList)
plt.ylabel('Month Number')
plt.xlabel('Sales units in numbers')
plt.show

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/IrisData/company_sales_data.csv")
monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
shampooSalesData = df['shampoo'].tolist()
moisturizerSalesData = df['moisturizer'].tolist()

# Labels up the plotted legend
plt.plot([],[],color='m', label='Face Cream', linewidth=5)
plt.plot([],[],color='c', label='Face Wash', linewidth=5)
plt.plot([],[],color='r', label='Tooth paste', linewidth=5)
plt.plot([],[],color='k', label='Bathing soap', linewidth=5)
plt.plot([],[],color='g', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)

#Stacks the plot
plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData, bathingsoapSalesData, shampooSalesData, moisturizerSalesData, colors=['m','c','r','k','g','y'])

#Asthetics
plt.xlabel('Month Number')
plt.ylabel('Sales units in Number')
plt.title('All product sales data using stack plot')
plt.legend(loc='upper left')
plt.show

# COMMAND ----------


