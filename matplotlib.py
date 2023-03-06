# Databricks notebook source
import matplotlib.pyplot as plt
import numpy as np
import pyspark as ps

# COMMAND ----------

# Basic figure
y = np.linspace(-1, 1, 5) #start at -1 to 1 with 5 equal spaces
x = np.arange(5) #

fig = plt.figure()
ax = fig.subplots()

line1 = ax.plot(x,y)

y2 = np.linspace(-2, 2, 5)
line2 = ax.plot(x,y2)

# COMMAND ----------

number_rows = 3
number_columns = 2
fig2 = plt.figure()
ax2 = fig2.subplots(number_rows,number_columns)
ax2[0,1].plot(x,y)

# COMMAND ----------

y1 = np.arange(0,110,10)
y2 = np.random.random(11)
x = np.arange(11)

fig, ax = plt.subplots(2,2)
ax[0,0].plot(x,y1)
ax[0,1].scatter(x,y2)
ax[1,0].bar(x,y1)
ax[1,1].barh(x,y1)

# COMMAND ----------

x = np.arange(0, 4+np.pi, 0.05)
ycos = np.cos(x)
ysin = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, ycos, 'b-', label="cos(x)")
ax.plot(x, ysin, 'r--', label="sin(x)")

ax.set_title("Trigonometric functions")
ax.set_xlabel("0 to 4pi")
ax.set_ylabel("cos(x) and sin(x)")
ax.legend()

# COMMAND ----------

fig, ax =plt.subplots(1,2)

# Horizontal (plot)
ax[0].axhline(0.3, color='red')
ax[0].axhline(0.4, linestyle='--', color='blue')
ax[0].axhline(0.5, color='cyan', linewidth=19)
ax[0].axhline(0.6, linestyle=':', xmin=0.25, xmax=0.75, color='orchid')
ax[0].axhline(0.7, xmin=0.25, xmax=0.75, color=(0.1, 0.2, 0.5, 0.3))

# Vertical (plot)
ax[1].axvline(0.3, color='red')
ax[1].axvline(0.4, linestyle='--', color='blue')
ax[1].axvline(0.5, color='cyan', linewidth=19)
ax[1].axvline(0.6, linestyle=':', ymin=0.25, ymax=0.75, color='orchid')
ax[1].axvline(0.7, ymin=0.25, ymax=0.75, color=(0.1, 0.2, 0.5, 0.3))

# Set x-axis and y-axis limits
ax[0].set_ylim([0.1, 0.9])
ax[1].set_xlim([0.1, 0.9])


# Set title to figure and subplots
fig.suptitle("Horizontal and Vertical lines", fontsize=14)
ax[0].set_title('Horizontal lines', fontstyle='italic')
ax[1].set_title('Vertical lines', color='green', fontname='Arial')



# COMMAND ----------

# Random list data(inputed manually)
x = np.array([2,3,6,7,4,2,5,7,8,9,4,2,1])
y = np.array([7,5,4,1,6,7,8,1,9,5,9,3,5])

fix, ax = plt.subplots(1,3) # How many graphs you having and in which axis

# Configuration of 1st graph
ax[0].scatter(x,y)
ax[0].set_title('default')


# Configuration of 2nd graph
ax[1].scatter(x, y, 50, marker='+')
ax[1].set_title('size = 50, style= +')


# Configuration of 3rd graph
crosses = ax[2].scatter(x, y, 200, marker='+', linewidth=3)
bullets = ax[2].scatter(x, y, 50, marker='o', color='black')
bullets.set_edgecolors('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')




# COMMAND ----------

# 3D dimensional graphs
z = np.array([0,1,4,3,5,1,2,5,7,5,9,8,5])
fig = plt.figure()
ax = np.array([fig.add_subplot(1,3,1, projection ='3d'),
              fig.add_subplot(1,3,2, projection ='3d'),
              fig.add_subplot(1,3,3, projection ='3d')])

# 1st Graph
ax[0].scatter(x,y,z)
ax[0].set_title('default')

# 2nd Graph
ax[1].scatter(x,y,z, s=50, marker='+')
ax[1].set_title('size = 50, style = +')

# 3rd Graph
crosses = ax[2].scatter(x,y,z, s=200, marker='+', linewidth=3)
bullets = ax[2].scatter(x,y,z, s=50, marker='o', color='black')
bullets.set_edgecolor('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')

# COMMAND ----------

# Data
people = ["Student A" , "Student B"]
studentA = np.array([90,50,80,40]) # Raw data sample for first Graph
studentB = np.array([75,45,60,65]) # Raw data sample for second graph
x = np.arange(len(studentA))
 
# Figure
fig, ax = plt.subplots(1,2)

# Plots
ax[0].bar(x, studentA, width=0.4) # Display Bar plot + it's width
ax[1].bar(x, studentB, width=0.4) # Display Bar plot + it's width
ax[0].set_title('Student A')
ax[1].set_title('Student B')

#Aesthetics
for i in range(len(ax)):
    ax[i].set_ylim(0,100) # Data range from 0-100
    ax[i].set_title(people[i])
    ax[i].set_xlabel("excercise") #bottom label
    ax[i].set_ylabel("mark (%)") # side lable
    ax[i].set_xticks([0,1,2,3])  #splits into 4 different columns
    ax[i].set_xticklabels(["ex1", "ex2", "ex3", "ex4"]) # labels each column
    
# Extra: Fixes subplots seperation (makes it bigger/expands so it's easier to read)
fig.tight_layout()


# Bar plot with the same data
fig, ax = plt.subplots() # Takes data figure array
width = 0.3 # Sets bar width
s1bars = ax.bar(x - width/2, studentA, width, label="Student A")
s2bars = ax.bar(x + width/2, studentB, width, label="Student B")

fig.tight_layout()

# COMMAND ----------

# Data
people = ["Student A", "Student B"]
studentA = np.array([90, 50, 80, 40])
studentB = np.array([75, 45, 60, 95])
x = np.arange(len(studentA))

fig, ax = plt.subplots()
width = 0.34

s1bars = ax.bar(x - width/2, studentA, width, label='Student A')
s2bars = ax.bar(x + width/2, studentB, width, label='Student B')

#Aesthetics
ax.set_title("Student Performance Chart")
ax.set_ylim(0,100) 
ax.set_xlabel("Excercise")
ax.set_ylabel("Score") 
ax.set_xticks([0,1,2,3])  
ax.set_xticklabels(["ex1", "ex2", "ex3", "ex4"])

# sets Line width and colours it red if score falls below 50    
for i in range(len(studentA)):
    s1bars[i].set_linewidth(3.5)
    s2bars[i].set_linewidth(3.5)
    if studentA[i] <50:
        s1bars[i].set_edgecolor('red')
    if studentB[i] <50:
        s2bars[i].set_edgecolor('red')
    

fig.tight_layout()

# COMMAND ----------

dataRaw= spark.read.csv(path= "dbfs:/FileStore/IrisData/iris_head_num.txt") #find file path
dataRaw= np.array(dataRaw.select("*").collect()) #collects data
header = dataRaw[0,:]
data = dataRaw[1:, :4]
data = np.vstack(data.astype(np.float32))

labels = np.vstack(dataRaw[1:, 4].astype(np.int32))

labelsUn, labelsCounts = np.unique(labels, return_counts= 1)



# COMMAND ----------

nrows,ncols = np.shape(data)
nclasses = len(labelsUn)
average = np.zeros((nclasses,ncols))
maxi = np.zeros((nclasses,ncols))
mini = np.zeros((nclasses,ncols))
sd = np.zeros((nclasses,ncols))
for i in labelsUn:
    indexes = np.reshape(labels==i, nrows)
    average[i-1,:] = np.mean(data[indexes,:], axis=0)
    maxi[i-1,:] =np.max(data[indexes,:], axis=0)
    mini[i-1,:] =np.min(data[indexes,:], axis=0)
    sd[i-1,:] =np.std(data[indexes,:], axis=0)

# COMMAND ----------

species = np.array(['Setosa', 'Versicolo', 'Virginica'])
features = np.array(header[:-1].astype("U"))
x = np.arange(len(features))

fig, ax = plt.subplots()
for i in labelsUn:
    ax.errorbar(x, average[i-1,:], sd[i-1,:], marker= "o", label=species[i-1])

# Aesthetics
ax.legend(loc= "upper right") # Groups each species names together and puts in top right corner
ax.set_xlabel("Features", fontsize=14, fontweight='bold') #labels x axis
ax.set_ylabel("mean +/- sd", fontsize=14, fontweight='bold') # labels y axis
ax.set_xticks(x) # set ticks in x axis
ax.set_xticklabels(features, rotation=45) # each tick gets labeled
fig.tight_layout() # ensure data is more spreadout



# COMMAND ----------

# Boxplots (2)
outliers = dict(marker= '+', markerfacecolor='black')
medians = dict(linewidth=2) 
boxes = np.array([dict(facecolor='r', color='r'),
                 dict(facecolor='g', color='g'),
                 dict(facecolor='b', color='b')])

mylegend = [plt.scatter([0],[0], facecolor='r', edgecolor='r', label=species[0]),
            plt.scatter([0],[0], facecolor='g', edgecolor='g', label=species[1]),
            plt.scatter([0],[0], facecolor='b', edgecolor='b', label=species[2])]
plt.close #make sure that no figure is generated

x = -7
step = 5
fig, ax = plt.subplots()

for j in range(len(features)):#for each feature
    x+=7
    for i in labelsUn: #for each category
        indexes = np.reshape(labels==i, nrows)
        temp = data[indexes,j]
        ax.boxplot(temp, positions=[x],
                  widths = 2,
                  patch_artist=True,
                  medianprops=medians,
                  boxprops=boxes[i-1],
                  flierprops=outliers)
        x+= step

# Add all labels to graph 
ax.set_title("Iris Data Set", fontsize=13, fontweight='bold') #set fontsize and type
ax.set_ylabel("Values", fontweight='bold')
ax.set_xticks(np.arange(step, x, 22))
ax.set_xticklabels(features, fontweight='bold', rotation=45)
ax.legend(handles=mylegend)
fig.tight_layout() #Make sure that the axis labels fit the figure


# COMMAND ----------


