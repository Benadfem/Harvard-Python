#this project pratice the use of Match and case
name = input("Who do you want to say hi to? ")

#now we can use the match case now
match name:
    case "Benson":
        print(f"welcome The Chairman")
    case _:
        print(f"You are not the chairman {name}")