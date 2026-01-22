# #program to test a code if it will run
# numbers_in_string= "1235-6548-9"
#
#
# print(len(numbers_in_string))
# for index in numbers_in_string:
#     if index == "-":
#         pass
#     else:
#         print(index)

#A program to test the value and ref of a dictionary

# capitals = {"Nigeria" : "Abuja",
#             "USA": "Washington D.C"}
#
# # print(capitals["Ghana"])
# print(capitals.get("Ghana","Country not found"))


# camel.py

def main():
    # Prompt the user for the variable name in camelCase
    camel_input = input("camelCase: ")

    # Print the start of the output
    print("snake_case: ", end="")

    # Iterate over every character in the string
    for char in camel_input:
        # Check if the character is uppercase
        if char.isupper():
            # If uppercase, print underscore and the lowercase version
            print("_" + char.lower(), end="")
        else:
            # Otherwise, just print the character
            print(char, end="")

    # Print a new line at the end
    print()

if __name__ == "__main__":
    main()
