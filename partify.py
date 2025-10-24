def main():
    x = int(input("What's X? "))

    if is_Even(x):
        print("Even")
    else:
        print("Odd")

#this new version of coding in python 
#it makes conditional so explicit than the use of if and elif, 
def is_Even(n):
    return n % 2 == 0

main()