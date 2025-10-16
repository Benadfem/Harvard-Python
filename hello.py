#Passing argument to function by 
# telling the user to input thier name

#Ask the user for thier name and removing the white spaces and Capitalizing the name
name = input("What's your name? ").strip().title()


#Greeting the usser only with the first name 
first, last =name.split()
#Say Hello to User!
# Added the F string formatting 
print(f"Hello, {first}")
