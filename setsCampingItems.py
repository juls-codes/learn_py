#Jullianne Biay
#Date created: October 31, 2022
#Program to display objects in sets 

inputA = input("Items for camperA: ")
inputB = input("Items for camperB: ")

#split strings into a list (split by comma)
listA = []
listB = []

for x in inputA:
    inputA = inputA.replace(' ', '')
    listA.extend(inputA.split(','))

for x in inputB:
    inputB = inputB.replace(' ', '')
    listB.extend(inputB.split(','))

    
#convert list to a set
setA = set(listA)
setB = set(listB)

#display each camper's set
print("Items for camperA: ")
for x in setA:
    print(x)

print("Items for camperB: ")
for x in setB:
    print(x)

#display all items, no repitition
print("All camping items: ")
for x in setA|setB:
    print(x)
    
#display common items
print("Common items between the campers: ")
for x in setA&setB:
    print(x)
    
#display unique items
print("Unique items to each camper: ")
for x in setA^setB:
    print(x)
