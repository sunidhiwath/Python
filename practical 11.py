import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv("sales_data.csv")

# -------------------------------
# a) Total profit of all months (Line Plot)
# -------------------------------
plt.figure()
plt.plot(df['month_number'], df['total_profit'], marker='o')
plt.title("Total Profit Per Month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

# -------------------------------
# b) All product sales (Multiline Plot)
# -------------------------------
plt.figure()
plt.plot(df['month_number'], df['facecream'], label='Face Cream')
plt.plot(df['month_number'], df['facewash'], label='Face Wash')
plt.plot(df['month_number'], df['toothpaste'], label='Toothpaste')
plt.plot(df['month_number'], df['bathingsoap'], label='Bathing Soap')
plt.plot(df['month_number'], df['shampoo'], label='Shampoo')
plt.plot(df['month_number'], df['moisturizer'], label='Moisturizer')

plt.title("Sales Data of All Products")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.legend()
plt.show()

# -------------------------------
# c) Face cream & face wash (Bar Chart)
# -------------------------------
plt.figure()
x = df['month_number']
width = 0.3

plt.bar(x - width/2, df['facecream'], width=width, label='Face Cream')
plt.bar(x + width/2, df['facewash'], width=width, label='Face Wash')

plt.title("Face Cream vs Face Wash Sales")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.legend()
plt.show()

# -------------------------------
# d) Total yearly sales per product (Pie Chart)
# -------------------------------
plt.figure()

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']
sales = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

plt.pie(sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Yearly Sales per Product")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# Step 1: Create Dataset
# -----------------------------------
companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS', 'Amdocs']
recruitments = [120, 150, 180, 90, 110, 130, 70, 95]

df = pd.DataFrame({
    'Company': companies,
    'Recruitment': recruitments
})

# -----------------------------------
# a) Bar Chart
# -----------------------------------
plt.figure()
plt.bar(df['Company'], df['Recruitment'])
plt.title("Company Recruitment")
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=45)
plt.show()

# -----------------------------------
# b) Pie Chart
# -----------------------------------
plt.figure()
plt.pie(df['Recruitment'], labels=df['Company'], autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# -----------------------------------
# c) Customized Pie Chart
# -----------------------------------
plt.figure()
colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'yellow', 'cyan']
explode = [0.1, 0, 0, 0, 0, 0, 0, 0]

plt.pie(df['Recruitment'],
        labels=df['Company'],
        autopct='%1.1f%%',
        colors=colors,
        explode=explode,
        shadow=True)

plt.title("Customized Pie Chart")
plt.show()

# -----------------------------------
# d) Doughnut Chart
# -----------------------------------
plt.figure()
plt.pie(df['Recruitment'], labels=df['Company'], autopct='%1.1f%%')

# Draw white circle in center
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Doughnut Chart")
plt.show()

# -----------------------------------
# e) Compare IBM & Amdocs
# -----------------------------------
plt.figure()

ibm = df[df['Company'] == 'IBM']['Recruitment'].values[0]
amdocs = df[df['Company'] == 'Amdocs']['Recruitment'].values[0]

plt.bar(['IBM', 'Amdocs'], [ibm, amdocs])
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.ylabel("Recruitment Count")
plt.show()