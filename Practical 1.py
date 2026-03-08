# Employee Salary Calculation

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
department = input("Enter department: ")
basic_salary = float(input("Enter basic salary: "))

DA = 0.92 * basic_salary
HRA = 0.58 * basic_salary
TA = 0.30 * basic_salary
LIC = 500

total_salary = basic_salary + DA + HRA + TA - LIC

print("\nEmployee Details")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)

print("\nSalary Details")
print("Basic Salary:", basic_salary)
print("DA:", DA)
print("HRA:", HRA)
print("TA:", TA)
print("LIC Deduction:", LIC)
print("Total Salary:", total_salary)

# Vendor Purchase Report

name = input("Enter vendor name: ")
year = input("Enter year of association: ")
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

print("\nEnter monthly purchase amounts")

total = 0

for i in range(1, 13):
    amount = float(input(f"Month {i} purchase: "))
    total += amount

print("\nVendor Details")
print("Name:", name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)

print("Total Annual Purchase:", total)