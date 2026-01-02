import pandas as pd
import numpy as np

# Task 1
##############
task1_data_frame = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
})
print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print(task1_with_salary)

task1_older =  task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print(task1_older)

task1_older.to_csv("employees.csv", index=False)

# Task 2
##############
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000},
]

# create JSON file 
pd.DataFrame(additional_employees).to_json(
    "additional_employees.json",
    orient="records",
    indent=2
)

json_employees = pd.read_json("additional_employees.json")
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# Task 3
#################

first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

more_employees.info()

# Task 4
#################

dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)

clean_data = dirty_data.copy()

# remote dublicate
clean_data = clean_data.drop_duplicates()
print(clean_data)

# Age
if "Age" in clean_data.columns:
    clean_data["Age"] = clean_data["Age"].replace(["unknown", "n/a", "NaN", ""], pd.NA)
    clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)

# Salary
if "Salary" in clean_data.columns:
    clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a", "NaN", ""], pd.NA)
    clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

# Age mean, Salarary median
if "Age" in clean_data.columns:
    clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())

if "Salary" in clean_data.columns:
    clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print(clean_data)

# datetime
for col in ["Hire Date", "HireDate", "Hire_Date"]:
    if col in clean_data.columns:
        clean_data[col] = pd.to_datetime(clean_data[col], errors="coerce")
        clean_data[col] = clean_data[col].fillna(method="ffill")
        break
print(clean_data)

# strip and uppercase
if "Name" in clean_data.columns:
    clean_data["Name"] = clean_data["Name"].astype("string").str.strip().str.upper()

if "Department" in clean_data.columns:
    clean_data["Department"] = clean_data["Department"].astype("string").str.strip().str.upper()

print(clean_data)








