txt_data = "I love Pizza"

# create a file path for the file.
path_file = "output.txt"


# create a file now
with open(path_file, "w") as file:
    file.write(txt_data)
    print(f"File {path_file} was created")