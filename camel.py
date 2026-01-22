# Ask user for input
camel_input = input("camelCase: ")

print("snake_case: ", end="")

for char in camel_input:
    if char.isupper():
        # If it is a Capital letter, print underscore + lowercase
        print("_" + char.lower(), end="")
    else:
        # If it is small letter, print it as is
        print(char, end="")

# Print a final empty line so the terminal looks clean
print()