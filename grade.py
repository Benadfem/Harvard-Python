#this is a program that displays the grade of a candidate
def main():
    score = int(input("Enter your score "))

    print(grade(score))

def grade(n):
    #now it is time to determine the grade of the student 
    if n >= 75 and n <=100:
        return f"Your grade is A"
    elif n >=60  and n <=74 :
        return f"Your grade is B"
    elif n >= 50 and n <= 59 :
        return f"Your grade is C"
    elif n >= 40 and n <=49:
        return f"Your grade is D"
    else:
        return f"You failed. try again next year!"

main() 