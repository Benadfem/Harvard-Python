#the game distribute 100 bottles of beer among friends until it finishes


import time
total_number = 10
count_down = 1

while total_number >= count_down :
    number_bottles = "Bottles"
    if total_number ==1:
        number_bottles = "Bottle"
    print(f"{total_number} {number_bottles} of beer on the wall, {total_number} {number_bottles} of beer.")

    total_number-=1
    print(f"Take one down and pass it around, {total_number} {number_bottles} of beer on the wall.")
    print()
    # count_down+=1
    time.sleep(1)
print("No more bottles on the wall, no more {bottles} of beer")
print(f"Go to the store and get {total_number} bottles of beer")

