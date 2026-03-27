import pandas as pd

# Create the DataFrame manually (based on given data)
data = {
    "carat": [0.23, 0.21, 0.23, 0.29, 0.31],
    "cut": ["Ideal", "Premium", "Good", "Premium", "Good"],
    "color": ["E", "E", "E", "I", "J"],
    "clarity": ["SI2", "SI1", "VS1", "VS2", "SI2"],
    "depth": [61.5, 59.8, 56.9, 62.4, 63.3],
    "table": [55.0, 61.0, 65.0, 58.0, 58.0],
    "price": [326, 326, 327, 334, 335],
    "x": [3.95, 3.89, 4.05, 4.20, 4.34],
    "y": [3.98, 3.84, 4.07, 4.23, 4.35],
    "z": [2.43, 2.31, 2.31, 2.63, 2.75]
}

df = pd.DataFrame(data)

# i) Mean price for each cut
mean_price = df.groupby("cut")["price"].mean()
print("Mean price for each cut:")
print(mean_price)

# ii) Count, minimum and maximum price for each cut
stats = df.groupby("cut")["price"].agg(['count', 'min', 'max'])
print("\nCount, Min and Max price for each cut:")
print(stats)

# iii) Average of x, y, z separately
avg_x = df["x"].mean()
avg_y = df["y"].mean()
avg_z = df["z"].mean()

print("\nAverage values:")
print("x:", avg_x)
print("y:", avg_y)
print("z:", avg_z)
import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
automotive_emp = df[df["Department"] == "Automotive"]
print("Employees in Automotive domain:")
print(automotive_emp)

# b) Employee details by ID (user input)
emp_id = int(input("\nEnter Employee ID: "))
emp_details = df[df["Employee ID"] == emp_id]

print("\nEmployee Details:")
print(emp_details)

# d) List of all Developers
developers = df[df["Designation"] == "Developer"]
print("\nList of Developers:")
print(developers)