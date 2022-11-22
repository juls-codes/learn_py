#Program for demonstrating standard library functions

import statistics

#Python 3 will convert integers to floats as needed
list = []

while True:
    userInput = input('Enter a number: ')

    if userInput == '':
        break

    try:
        list.append(float(userInput))
        
    except ValueError: #ensures only numbers for input
        print('Invalid input. Please enter a float or an integer.')
        continue


print(f"Sum: {sum(list)}")
print(f"Mean: {statistics.mean(list)}")
print(f"Median: {statistics.median(list)}")

