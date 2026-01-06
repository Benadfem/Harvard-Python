# #program to test a code if it will run
# numbers_in_string= "1235-6548-9"
#
#
# print(len(numbers_in_string))
# for index in numbers_in_string:
#     if index == "-":
#         pass
#     else:
#         print(index)

#A program to test the value and ref of a dictionary

capitals = {"Nigeria" : "Abuja",
            "USA": "Washington D.C"}

# print(capitals["Ghana"])
print(capitals.get("Ghana","Country not found"))
