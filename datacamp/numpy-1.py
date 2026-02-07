""" python_list = [1, 2, 3, 4, 5]
import numpy as np
numpy_array = np.array([1, 2, 3, 4, 5])
python_list + python_list
numpy_array + numpy_array
# Output:
print("Python List Addition:", python_list + python_list)
print("Numpy Array Addition:", numpy_array + numpy_array)

# Import the numpy package as np
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball

np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))


print(np.array([True, 1, 2]) + np.array([3, 4, False]))
weight_lb = [180, 215, 210, 210, 188, 176, 209, 200, 190, 175, 185, 205, 220, 199, 202, 207, 213, 198, 182, 177, 195, 208, 212, 214, 219, 221, 178, 183, 186, 187, 189, 191, 192, 193, 194, 196, 197, 201, 203, 204, 206, 211, 215, 217, 218, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249 ]
height_in = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 69, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

array_2d = np.array([[1, 2, 3, 23, 5.2, 6.4],
                     [43, 55, 61, 2.3, 5.4, 6.5]])

print(array_2d[1, :])  # Prints the second row
print(array_2d[:, 2])  # Prints the third column
print(array_2d[:, 1:3])  # Prints all rows and columns 1 to 2

print(array_2d.shape)

# ##### new task

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball

print(np_baseball[49, :])

# Select the entire second column of np_baseball: np_weight_lb

np_weight_lb = np_baseball[:, 1]

# Print out height of 124th player

print(np_baseball[123, 0])


# Create np_height_in from np_baseball

np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in

print(np.mean(np_height_in))

# Print out the median of np_height_in

print(np.median(np_height_in))

### tasks at 03/02/2026
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

import matplotlib.pyplot as plt

year = [1960, 1980, 2000, 2020]
pop = [3.02, 4.44, 6.08, 7.79]
plt.plot(year, pop)
plt.xlabel("Year")
plt.ylabel("Population (billions)")
plt.show()


plt.scatter(np_baseball[:,0], np_baseball[:,1])
plt.xlabel("Height (in)")
plt.ylabel("Weight (lbs)")
plt.show()


### task about matplotlib
# Print the last item from year and pop

print(year[-1], pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis

plt.plot(year, pop)

# Display the plot with plt.show()

plt.show()
#### TASK about scatter plot
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()


#### TASK
# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop, life_exp)


# Show plot
plt.show()

#### TASK
# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

#### TASK
# Build histogram with 5 bins
plt.hist(life_exp, bins = 5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clean up again
plt.show()
plt.clf()

##### TASK
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title

plt.title(title)
# After customizing, display the plot
plt.show()


#### TASK
# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()


##### TASK
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = 2 * np_pop

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

#### TASK
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()
#### TASK
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call

plt.grid(True)
# Show the plot
plt.show()


##### TASK

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europ
europe["italy"] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe["poland"] = 'warsaw'

# Print europe
print(europe)


##### TASK

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia

del(europe['australia'])

# Print europe
print(europe)


##### TASK

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data

data = {'capital':'rome', 'population':59.83}
# Add data to europe under key 'italy'

europe['italy'] = data
# Print europe
print(europe)
 """
# Пояснення як працює код для суми стовпців у 2D масиві
import numpy as np
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12],
          [13, 14, 15],
          [16, 17, 18],
          [19, 20, 21]]

arr = np.array(matrix)
column_sums = np.sum(arr, axis=0)
print(column_sums)  # sums of each of the 3 columns separately
# Відповідно порахувати суму для кожної строки можна так:
arr = np.array(matrix)
row_sums = np.sum(arr, axis=1)
print(row_sums)  # sums of each of the 7 rows separately
