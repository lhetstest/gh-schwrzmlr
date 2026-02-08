'''
# While loops:
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else :
      offset = offset + 1
    print(offset)

# For loops:
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for i in areas:
    print(i)

#example with indexes:
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Change for loop to use enumerate() and update print()
for index,a in enumerate(areas) :
    print("room " + str(index) + ": " + str(a))

#Adapt the print() function in the for loop so that the first printout becomes "room 1: 11.25", the second one "room 2: 18.0" and so on.
# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))


# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for index, sqm in enumerate(house):
    print("the " + str(sqm[0]) + " is " + str(sqm[1]) + " sqm")

#For loop for dictionary:
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }
# Iterate over europe
for key, value in europe.items() :
    print("the capital of " + key + " is " + value)

#for loop for 2D list:
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
for value in bmi :
    print(value)

meas = np.array([np_height, np_weight])
#to get every element in the 2D array:
for val in np.nditer(meas) :
    print(val)


# task for loops:
# Import numpy as np
import numpy as np

# For loop over np_height
for i in np.nditer(np_height):
    print(str(i) + " inches")

# For loop over np_baseball
for s in np.nditer(np_baseball):
    print(s)
'''

import pandas as pd
# exaple of iteration through DataFrame:
# import 5 countries, their capitals, population and area into a DataFrame
data = {'country': ['Spain', 'France', 'Germany', 'Norway', 'Italy'],
        'capital': ['Madrid', 'Paris', 'Berlin', 'Oslo', 'Rome'],
        'population': [46.77, 66.03, 80.62, 5.084, 59.83],
        'area': [505990, 640679, 357578, 385203, 301340]}
countries = pd.DataFrame(data, index=['ESP', 'FRA', 'GER', 'NOR', 'ITA'])
print(countries)
# Iterate over DataFrame and print country and capital

for lab, row in countries.iterrows() :
    countries.loc[lab, "name_length"] = len(row['country'])
print(countries)
# more efficient way with apply():
countries["name_length"] = countries["country"].apply(len)
print(countries)

# TASK:
# Write a for loop that iterates over the rows of cars and on each iteration perform two print() calls: one to print out the row label and one to print out all of the rows contents.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)

#Using the iterators lab and row, adapt the code in the for loop such that the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on.
#The output should be in the form "country: cars_per_cap". Make sure to print out this exact string (with the correct spacing).
#You can use str() to convert your integer data to a string so that you can print it in conjunction with the country label.
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))

# Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. You can use the string method upper() for this.
# To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
print(cars)
#Replace the for loop with a one-liner that uses .apply(str.upper). The call should give the same result: a column COUNTRY should be added to cars, containing an uppercase version of the country names.
#As usual, print out cars to see the fruits of your hard labor
cars["COUNTRY"] = cars["country"].apply(str.upper)
#explaination: the .apply() method applies the function str.upper to each element in the "country" column, and the result is assigned to the new "COUNTRY" column.
#did the country column exist before I made apply? Yes, it did. It was created when we imported the data from the CSV file. The .apply() method is just transforming the existing "country" column and creating a new "COUNTRY" column with the transformed values.
print(cars)

#coin toss with rand.seed():
import numpy as np
np.random.seed(123)
# Simulate tossing a coin 10 times: 0 is tails, 1 is heads
coin_tosses = np.random.randint(0, 2, 10)
for toss in coin_tosses:
    if toss == 0:
        print("Tails")
    else:
        print("Heads")
print(coin_tosses)

# Import numpy as np
# Use seed() to set the seed; as an argument, pass 123.
# Generate your first random float with rand() and print it out.
import numpy as np

# Set the seed - this makes sure your "random" numbers are the same as mine! - so that we can check your answer.
np.random.seed(123)

# Generate and print random float

x = np.random.rand()
print(x)

#Use randint() with the appropriate arguments to randomly generate the integer 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out
#use randint to simulate a dice roll, which generates a random integer between 1 and 6 (inclusive). The arguments for randint should be 1 and 7, because the upper bound is exclusive.
# Set the seed
np.random.seed(123)
# Simulate a dice roll and print it out
dice_roll = np.random.randint(1, 7)
print(dice_roll)
# Repeat the outcome to see if the second throw is different. Again, print out the result.
dice_roll2 = np.random.randint(1, 7)
print(dice_roll2)

'''
Roll the dice. Use randint() to create the variable dice.
Finish the if-elif-else construct by replacing ___:
If dice is 1 or 2, you go one step down.
if dice is 3, 4 or 5, you go one step up.
Else, you throw the dice again. The number on the dice is the number of steps you go up.
Print out dice and step. Given the value of dice, was step updated correctly?
'''

# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)
# Starting step
step = 50

# Roll the dice

dice = np.random.randint(1, 7)
# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step

print(dice)
print(step)

#heads of tails
import numpy as np
np.random.seed(123)

outcomes = []
for x in range(10) :
    coin = np.random.randint(0, 2)
    if coin == 0 :
        outcomes.append("Heads")
    else :
        outcomes.append("Tails")

print(outcomes)

tails = [0]
for x in range(10) :
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
print(tails)

'''
Make a list random_walk that contains the first step, which is the integer 0.
Finish the for loop:
The loop should run 100 times.
On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
Next, let the if-elif-else construct update step for you.
The code that appends step to random_walk is already coded.
Print out random_walk.
'''
# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)
# Initialize random_walk
random_walk = [0]
# Complete the for loop
for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1, 7)
    if dice <= 2 :
        step = step - 1
    elif dice <= 5 :
        step = step + 1
    else :
        step = step + np.random.randint(1,7)
    random_walk.append(step)

# Print random_walk
print(random_walk)
