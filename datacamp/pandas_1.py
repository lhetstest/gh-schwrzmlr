# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

#### Example

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

#### Example

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JPN'])
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1, 6]])

#### Example

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars)
print(cars.iloc[[5],[2]])
# Print sub-DataFrame
print(cars.iloc[[4, 5],[1,2]])


# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame

print(cars.loc[:, ['cars_per_cap','drives_right']])
print(cars.iloc[:, [0, 2]])


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
#use the boolean Series dr to filter rows in the cars DataFrame, and save the filtered DataFrame in a new variable sel.
sel = cars[dr]

# Print sel
print(sel)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500

car_maniac = cars[cars["cars_per_cap"] > 500]
print(car_maniac)


### RECAP
'''
Square Brackets:

Single square brackets ([]) return a Pandas Series.
Double square brackets ([[]]) return a Pandas DataFrame.
Example:
cars['country']  # Series
cars[['country']]  # DataFrame
Selecting Rows with Slicing:

Use slices to select specific rows.
Example:
cars[0:3]  # First three rows
loc and iloc:

loc is label-based, using row and column labels.
iloc is index-based, using integer positions.
Example:
cars.loc['RU']  # Row for Russia using label
cars.iloc[4]  # Row for Russia using index
Combining Rows and Columns:

Use loc and iloc to select specific rows and columns simultaneously.
Example:
cars.loc[['RU', 'MOR'], ['country', 'drives_right']]  # Specific rows and columns
'''
