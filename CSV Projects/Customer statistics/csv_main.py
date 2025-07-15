import pandas as pd

sales = pd.read_csv(r'CSV Projects\Customer statistics\sales.csv')
location = (sales.groupby('location'))
sales_location = (sales.groupby('location')["sales"])
grouped = sales.groupby('location')["sales"].sum()
mean = sales.groupby('location')["sales"].mean()
median = sales.groupby('location')["sales"].median()

# ---------------------------------------------------- #

for loc in location:
    print(f"location:\n {loc}")

print("-" * 20)

for sel_loc in sales_location:
    print(f"sales_location:\n {sel_loc}")

print("-" * 20)

print(f"grouped:\n {grouped}")

print("-" * 20)

print(f"mean:\n {mean}")

print("-" * 20)

print(f"median:\n {median}")

print("-" * 20)
