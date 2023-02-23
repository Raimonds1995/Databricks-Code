# Databricks notebook source
print("hello world")

# COMMAND ----------

number1 = input("please enter a number")
number2 = input("enter a second")

print(int(number1) + int(number2))

# COMMAND ----------

varName = "varibable"
var2Name = 14

var2Name += 2

print(var2Name)

# COMMAND ----------

num1 = 12
num2 = 23

print(num1 == num2)
print(num1 < num2)
print(num1 > num2)
print(num1 !=num2)
print(num1 <=num2)
print(num1 >= num2 and 10> 11)

if num1 > num2:
    print("First number is greater")
elif num1== num2:
    print("The numbers are equal")
else:
    print("the second number is greater")



# COMMAND ----------

num1 = int (input("enter first number"))
num2 = int (input("enter the second number"))

if num1 > num2:
    print("First number is greater")
elif num1 == num2:
    print("the numbers are equal")
else:
    print("Second is a larger number")


# COMMAND ----------

num1 = int (input("Enter Birth Year: "))

if num1 % 4 == 0 :
    print(num1, " Is a leap year")
else:
    print(num1, "Not a leap year")


# COMMAND ----------

#           0,1,2,3,4,5,6,7,8,9
products = [1,2,3,4,5,6,7,8,9,10]

for counter in range(len(products)):
    print(counter,products[counter])

# COMMAND ----------

count = 1
while count <10:
    print(count)
    count += 1

# COMMAND ----------

password = "opensesame1!"
count = 0
entry = False
while attemps <5:
while entry != password:
    entry= input("Please enter your password")
    print("wrong password")
    
print("Welcome in")

# COMMAND ----------

total = 0
while True:
    guess = input("Please  enter a number")
    if(int(guess)== 0):
        break
    else:
        total += int(guess)
        print("Current Total:", total)
    print(total)

# COMMAND ----------

guess = True
while guess == input("guess my name"):
    guess != "lord"
    print("correct")
    break
    print("wrong")
    break
    
    

# COMMAND ----------

attemps = 0

while attemps < 3:
    username = input ("Enter your username")
    password = input ("Enter your password")
    
    if username == "admin" and password == "admin123":
        print("Your login was successful")
        break
    else:
        print("Wrong Login or Password, Please try again")
        attemps += 1
        

# COMMAND ----------

import random

num = 3.1473

print(round(num, 2))
print(eval("num + 1"))

print(random.randint(1,100))


# COMMAND ----------

#def square(message):
    #print("message")
    
# def goodbye():
    #print("Goodbye World")
    
#square()
#goodbye()


def printMessage(message):
    print(message)
    
printMessage("Hello Wolrd")
printMessage("Goodbye Wolrd")


# COMMAND ----------

GlobalScope = True


def square(number):
    squaredNumber = number ** 2
    return squaredNumber

numToSquare = 5

answer = square(4)

print("The square root of 4 is:", answer)

# COMMAND ----------

def poundsToMetric(pounds):
    kilograms = pounds / 2.2
    grams = kilograms * 1000
    return int(kilograms), grams % 1000
    
pounds = float(input("How many pounds"))
kg, grams = poundsToMetric(pounds)
print("answer is : " ,pounds, kg, grams)


    


# COMMAND ----------

def convert(number):
    conversion = (number - 32) * 5/9
    return conversion

num_to_convert = 100

answer = convert(num_to_convert)

print("the celcious equivalent of " + str(num_to_convert) + "degress is" , answer, "degrees")

# COMMAND ----------

number_to_conv = 10

#function will accept Boolean:
#True: convert c -> f
#False: convert f -> c
def temp_converter(num, bool):
    if(bool == False):
        return((num - 32) * 5/9)
    else:
        return ((num * 1.8) +32)
    
temp_converter(16, True)  


print("converting" + str(number_to_conv) + " to C : ", temp_converter(number_to_conv, False))
print("converting" + str(number_to_conv) + " to F : ", temp_converter(number_to_conv, True))

# COMMAND ----------

list1 = [1,2,3,4,5, "strings", True , False]

list1.append("hello world")


print(list1)

# COMMAND ----------

list1 = [[1,2,3]], [4,5,6], [7,8,9]

# 1,2,3
# 4,5,6
# 7,8,9

print(list1[2])


# COMMAND ----------

import random

my_list = ["a", "b", "c'" "s"]

#del my_list[2:4]
#my_list[1] = "f"
#new_list = ["s"] + my_list
#new_list.append("g")

#new_list.insert(1, "t")

#letter = random.choice(new_list)

#print(letter)


final_list = []
for i in my_list:
    print(i, my_list.index(i))
    final_list.append(my_list.index(i))
    
print(final_list)

print(sum(final_list))
print(len(final_list))










# COMMAND ----------


list = []
for i in range(10):
    num = int(input("Enter a Number"))
    list.append(num)
    print(list)
    print("Total Sum =", sum(list))
    
    

# COMMAND ----------

word = "cats"

def is_plural(word):
    return word.endswith('s')
print(word)

# COMMAND ----------

number_list = [1,2,3,4,5,5,7]

def get_first_value(number_list):
    return number_list[0]
print(number_list[2])

# COMMAND ----------

list1 = [[1,2,3]], [4,5,6], [7,8,9]

# 1,2,3
# 4,5,6
# 7,8,9

print(list1[2])


# COMMAND ----------


