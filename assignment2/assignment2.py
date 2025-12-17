# Task 2 Read a CSV File
import csv
import traceback

def read_employees():
    """Reads employees.csv and returns a dictionary with 'fields' and 'rows'."""
    try:
        data = {"fields":[], "rows": [] }
        with open("../csv/employees.csv", "r" ) as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row
                else:
                    data["rows"].append(row)
        return data
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace =[]
        for trace in trace_back:
            stack_trace.append(
                f'File: {trace[0]}, Line: {trace[1]}, Func: {trace[2]}, Msg: {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)
                    

# Task 3 Find the Column Index

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")


# Task 4 Find the Employee First Name

def first_name(row_number):
    first_name_col =column_index("first_name")
    return employees["rows"][row_number][first_name_col]

# Task 5 Find the Employee: a Function in a Function

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches
    
# Task 6 Find the Employee with a Lambda

def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column])
                          == employee_id, employees["rows"]))
    return matches

# Task 7 Sort the Rows by last_name Using a Lambda

def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]

# Task 8 Create a dict for an Employee

def employee_dict(row):
    empl = {}
    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            empl[field] = row[index]
    return empl

# Task 9 A dict of dicts, for All Employees

def all_employees_dict():
    all_employees = {}
    for row in employees["rows"]:
        empl_id = row[employee_id_column]
        all_employees[empl_id] = employee_dict(row)
    return all_employees

# Task 10 Use the os Module

import os

def get_this_value():
    return os.getenv("THISVALUE")

# Task 11 Creating Your Own Module

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("abracadabra")
print(custom_module.secret)

# Task 12 Read minutes1.csv and minutes2.csv

import csv

def _read_minutes_file(path):
    data = {"fields": [], "rows": []}
    with open(path, "r", newline="") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                data["fields"] = row
            else:
                data["rows"].append(tuple(row))
    return data 
       
def read_minutes():
    minutes1 = _read_minutes_file("../csv/minutes1.csv")
    minutes2 = _read_minutes_file("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)


# Task 13 Create minutes_set

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()

# Task 14 Convert to datetime

from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)
    converted = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    )
    return converted

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15 Write out Sorted List

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    
    formatted = list(
        map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list)
    )

    with open("minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(formatted)

    return formatted

write_sorted_list
   




           

       
       
   







