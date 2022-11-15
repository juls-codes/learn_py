#Program for learning libraries
import numpy as np

# Multiply each element in list a with corresponding element in list b
# Result goes in list c
a = [2,4,6,8]
b = [3,4,5,6]
c = []

for i in range(len(a)):
    c.append(a[i] * b[i])
print("Using loop: ")
print(c)

e = np.array([2,4,6,8])
d = np.array([3,4,5,6])
f = np.array([])

f = d * e

print("Using numpy arrays")
print(f)
