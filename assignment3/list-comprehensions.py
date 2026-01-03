import csv

if __name__ == "__main__":
    # ti read CSV into a list of lists
    with open("../csv/employees.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        # Create list of full names 
        names = [row[0] + " " + row[1] for row in rows[1:]]
        print(names)

        # Names with letter "e"
        names_with_e = [name for name in names if "e" in name.lower()]
        print(names)

        

