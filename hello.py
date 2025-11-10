
def main():
    # call the function to action and adding the name of the user 
    name = input("What's your name> ")
    greeting = hello(name) + " How are you doing today?"
    print(greeting)


# writing hello program to be done using function 
def hello(to):
    # print(f"Hello, {to}")
    return f"Hello. {to}"

main()