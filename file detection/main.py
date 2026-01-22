import os

file_path = "STUFF/test.txt"

# check if the file path exists
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists' ")
else:
    print(f"The location '{file_path}' does not exists' ")

