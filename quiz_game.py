#this project is a quiz game
#this will set you on questions, grade you and give you percentage
questions = ("Which symbol is used in Python 3.14 to define a comment?",
             "Which of these is a mutable data type, essential for handling dynamic AI state?",
             "which feature allows code to run truly in parallel by disabling the Global Interpreter Lock?",
             "When building an AI agent with FastAPI, which keyword is used to pause execution while waiting for an API",
             "Which library is the industry standard in 2026 for strictly validating data schemas using Type Hints?",
             "Python 3.14 improved which feature to make debugging AI logic significantly easier for developers?",
             )
options = (("(A) //", "(B) /* */", "(C) #", "(D) $"),
           ("(A) Tuple", "(B) List", "(C) String", "(D) Float"),
           ("(A) Free-threading (No-GIL)",
            "(B) Multi-processing",
            "(C) JIT Compiler",
            "(D) Type Hinting"),
           ("(A) wait", "(B) defer", "(C) yield", "(D) await"),
           ("(A) Pandas", "(B) Numpy", "(C) Pydantic", "(D) Scikit-Learn"),
           ("(A) Variable naming", "(B) Error message hints", "(C) File saving", "(D) Screen brightness")
           )
answers = ("C", "B", "A", "D", "C", "B")
guesses = []
correct_guesses = []
option_index = 0

#give the count of the questions
count = 0
#print the questions in the question list
for question in questions:
    count += 1
    print(f"{count}. {question}")
    for option in options[option_index]:
        print(option)

    #now let's select the chosen options
    guess = input("choose from the options 'A-D': ").upper()
    guesses.append(guess)

    #check if the chosen option is correct
    if guess == answers[option_index]:
        #let's populate the correct_guesses list so we can track our success record
        correct_guesses.append(answers[option_index])
        print("----------CORRECT-------")

    else:
        print("----------INCORRECT-------")
        print(f"{answers[option_index]} is the correct answer")

    option_index += 1

print("------------------------")
print("--------RESULT----------")
print("------------------------")

#now let's get the result shown for the quiz
result = f"you score {len(correct_guesses)} out of {len(questions)} questions  correctly"
print(result)

#let us get the grade value of the student
grade = int((len(correct_guesses) / len(questions)) * 100)
print()
print(f"Your grade score is: {grade}%")
if grade >= 70:
    print("Your grade is A")
elif grade >= 60:
    print("Your grade is B")
elif grade >= 50:
    print("Your grade is C")
elif grade >= 40:
    print("Your grade is D")
elif grade > 0:
    print("Your grade is F")
else:
    pass
