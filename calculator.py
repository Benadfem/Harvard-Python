#define a main method to take up the application interfaces

def main():
    x = int(input("What's A "))
    y = int(input("What's Z "))

    print(condition(x,y))


# Always create a function to carry the functionality of your program
def condition(a,b):
    if a > b:
        return "A is greater B"
    elif a < b:
        return "A is less than B"
    else:
        return "A and B are equal"
    
main()