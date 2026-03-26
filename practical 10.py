import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("Complete Report:\n", df)

# b) Books by a given author
author_name = input("Enter author name: ")
print("\nBooks by", author_name)
print(df[df['Author'] == author_name])

# c) Books by a given publisher
publisher_name = input("\nEnter publisher name: ")
print("\nBooks by", publisher_name)
print(df[df['Publisher'] == publisher_name])

# d) Cheapest and costliest books
cheapest = df[df['Price'] == df['Price'].min()]
costliest = df[df['Price'] == df['Price'].max()]

print("\nCheapest Book:\n", cheapest)
print("\nCostliest Book:\n", costliest)

# e) Sort by year
sorted_df = df.sort_values(by='Year')
print("\nBooks sorted by Year:\n", sorted_df)

import pandas as pd

# Create data
data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "UP", "MP"],
    "Area": [307713, 196244, 342239, 243286, 308245],  # in sq km
    "Population": [124000000, 70000000, 81000000, 231000000, 85000000]
}

df = pd.DataFrame(data)

# a) Complete info
print("State Data:\n", df)

# b) State with largest area
print("\nState with Largest Area:")
print(df[df['Area'] == df['Area'].max()]['State'])

# c) State with largest population
print("\nState with Largest Population:")
print(df[df['Population'] == df['Population'].max()]['State'])

# d) Calculate population density
df['Density'] = df['Population'] / df['Area']
print("\nPopulation Density:\n", df[['State', 'Density']])

# e) State with highest density
print("\nState with Highest Population Density:")
print(df[df['Density'] == df['Density'].max()]['State'])