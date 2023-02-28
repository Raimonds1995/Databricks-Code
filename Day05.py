# Databricks notebook source
import numpy as np


# COMMAND ----------

my1dArray = np.array([1,2,3])
my2dArray = np.array([[1,2,3], [4,5,6]], dtype = float)
my2dArray = np.array(((1,2,3), (4,5,6)), dtype = np.float32)

charArray1 = np.array([(1, 'a', 3.), (4,5,'zzz')], dtype="U21")

print(charArray1)


# COMMAND ----------

rows = 4
cols = 3

array1s = np.ones((rows, cols))

array5s = 5 * np.ones((rows, cols)) 

array7s = np.full((rows, cols),7)

print(array1s)
print(array5s)
print(array7s)

# COMMAND ----------

samples = 3
step = 3
start = 10
stop = 25

np.arange(start, stop, step)

np.linspace(start, stop, samples)

np.eye(3)

np.random.random((2,3))

np.random.randint(0,10, (3,3))


# COMMAND ----------

a = np.array([[1,2,3], 
              [4,5,6], 
              [7,8,9]])

#a.ndim
#a.shape
#a.size
#a.dtype

#a[a < 9]
#np.diag(a)

summ1 = a.sum()
summ2 = np.sum(a, axis = 1)

print(summ1, summ2)




# COMMAND ----------

a = np.array([[1,2], [4,5]])
b = np.array([[9,8], [6,5]])

summ1 = a.sum()
summ2 = np.sum(a)

a + b
np.add(a, b)

a - b

a * b

a/b

np.exp(a)

np.sqrt(a)

np.sin(a)
np.cos(a)
np.log(a)

display(a.dot(b))


# COMMAND ----------

# (0,3)
# |\
# | \
# |  \
# |   \
# |____\ (1,5, 0)
# (0,0)

A = np.array([0,0])
B = np.array([0,3])
C = np.array([1.5,0])

# Compute AB
AB_diffSquared = np.power(A-B, 2)
AB_squared = np.sum(AB_diffSquared)
AB = np.sqrt(AB_squared)

# Compute AC

AC= np.sqrt(np.sum(np.power(A-C,2)))

# Compute BC

BC= np.sqrt(AB**2 + AC**2)


from numpy import linalg as la

AB2 = la.norm(A-B)

AC2 = la.norm(A-C)

BC2 = la.norm(B-C)

print(BC2, BC)




# COMMAND ----------

import numpy as np
# import pyspark as ps

# Use spark to read he text file as a csv
dataRaw = spark.read.csv(path = "dbfs:/FileStore/IrisData/iris_head_num.txt")
# Collect all the data and store it as a np array
dataRaw = np.array(dataRaw.select("*").collect())


# Seperate Date from headers
header = dataRaw[0:,]
# Select all rows except the first, all columns except the 4th
data = dataRaw[1:, :4]
# Convert data from string to float32
data = np.vstack(data.astype(np.float32))

# Select the labels columns
labels = np.vstack(dataRaw[1:, 4].astype(np.int32))

# Make an array of unique labels, and the number of labels total
labelsUn, labelsCounts = np.unique(labels, return_counts = 1)

# This show we have 3 different flowers in our dataset, with 50 samples each
display(labelsUn, labelsCounts)


# COMMAND ----------

# Find average, maximu, minimum and standard deviation for each cloum per category

# Number of rows(observation) and columns (attributes or features) of our data
nrows,ncols = np.shape(data) # > 150, 4
# Number of unique categories
nclasses = len(labelsUn) # > 3
#Initialise empty dfs into which we will update our statistics
average = np.zeros((nclasses,ncols))
maxi = np.zeros((nclasses,ncols))
mini = np.zeros((nclasses,ncols))
sd = np.zeros((nclasses,ncols))

for i in labelsUn: # > [1,2,3]
  #Select indices of where in df matches current label
    indexes = np.reshape(labels==i,nrows)
    #Push into empty arrays the calculated mean, max, min, and standardDeviation
    average[i-1,:] = np.mean(data[indexes,:],axis=0)
    maxi[i-1,:] = np.max(data[indexes,:],axis=0)
    mini[i-1,:] = np.min(data[indexes,:],axis=0)
    sd[i-1,:] = np.std(data[indexes,:],axis=0)
print(header)
print("averages")
print(average)
print("maximum")
print(maxi)
print("minimum")
print(min)
print("standard deviation")
print(sd)

# COMMAND ----------

# More optimal ways available but lets do it with nested for revision

# Make empty array to sotre outliers
outliers2sd = np.zeros((nclasses,ncols))
for i in labelsUn:
    #Find indexes again
    indexes = np.reshape(labels==i,nrows)
    #Select the data that matches ther class
    classData = data[indexes,:]
    #For each colum in this data
    for j in range(ncols):
        #Find threshold high and low
        thresholdLow = average[i-1,j]-2*sd[i-1,j]
        thresholdHigh = average[i-1,j]+2*sd[i-1,j]
        #Any data aboe or below
        remain = [x for x in classData[:,j] if(x > thresholdLow)]
        reamin = [x for x in classData[:,j] if(x < thresholdHigh)]
        #Calculate percentage of outliers
        outliers2sd[i-1,j] = 100 * (labelsCounts[i-1] - len(remain)) / labelsCounts[i-1]
        
print(header)
print(outliers2sd)

# COMMAND ----------

print(header)
print("averages")
print(average)
print("maximum")
print(maxi)
print("minimum")
print(min)
print("standard deviation")
print(sd)
print(outliers2sd)

# COMMAND ----------

# Export to spark.csv file
# some variables for formatting
decimals = 2
fmt = "%.2f"
formatf = ".csv"
import pandas as pd

# Our data is in all sort of shapes now after collecting it
# Well put it together, format it and export it.
species =np.array(['setosa','versicolor','virginica'])
header = dataRaw[0,:]
# For each of the flowers in our df
for i in range(len(labelsUn)):
    #Stack the statistics generated
    temp = np.vstack( [average[i,:], mini[i,:], maxi[i,:], sd[i,:], outliers2sd[i,:]] ).T
    
    #Round the deciamls to the nearest 2 places
    temp = np.around(temp,decimals)
    
    #Cast numbers to string and format
    temp_str = np.char.mod(fmt, temp)
    # Take header row and transpose it to be a column
    rows = np.array(header[:-1].astype("U"))[:, np.newaxis]
    
    # Put header column next to data
    print(rows, temp_str, header)
    rowsf = np.hstack((rows, temp_str))
    #make beauty header row for ther csv
    headerf = [species[i], 'mean', 'min', 'max', 'std', 'outliers2sd%']
    #Cast to pandas data frame, to then be cast to spark dataFrame
    pdDf = pd.DataFrame(rowsf, columns = [headerf])
    
    
    #Cast to spark dataFrame
    sparkDf = spark.createDataFrame(pdDf)
    #Try to write out 4 csvs
    try:
        sparkDf.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("dbfs:/FileStore/tables/irisTest/" + str(species[i]))
    except:
            #Unless file already exists
            print("File Already Exists")
    # Read back file to make sure everything works
    display(spark.read.csv("dbfs:/FileStore/tables/irisTest/" + str(species[i])))

# COMMAND ----------


