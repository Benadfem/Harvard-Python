import os

# import json module
import json

# let's create the employee data
employee = {
    "name": "Matthew",
    "Salary": 120000,
    "Job": "Manager"
}
# create a file path
file_path = "employee.json"

with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)
    print(f"json file {file_path} created")


