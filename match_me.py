def main():
    user_input = input("Write your expression ")

    x, y, z = user_input.split( )
    x = float (x)
    z = float(z)

    print(match_me(x, y, z))

def match_me (a , b , c):
    # global answer
    match b:
        case "+":
            answer = a + c
        case "-":
            answer = a - c
        case "*" :
            answer = a * c
        case "/" :
            answer = a / c
        case _ :
            answer = 'Enter valid arithemtic symbol '
    return f"{answer:.1f}"


main()
