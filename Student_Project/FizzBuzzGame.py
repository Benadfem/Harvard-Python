#A program that code a game
import time
for index in range(1,21):
    if index % 3 == 0 and  index % 5 == 0:
        print("FIZZBUZZ!")
    elif index % 5 == 0:
        print("BUZZ!")
    elif index % 3 == 0:
        print("FIZZ!")
    else:
        print(index)

    time.sleep(1)
print("Good game guys")