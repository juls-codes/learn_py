#Date created: October 31, 2022
#Program for demonstrating sets


itemsA = ()

user = input("Who are you?: ")
if (user == "camperA"):
    itemsA = {input("What are you bringing?: ")}
    print(itemsA)
   
elif (user == "camperB"):
    itemsB = {input("What are you bringing?: ")}
    print(itemsB)

else:
    user = input("Who are you?: ")
