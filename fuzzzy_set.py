A1 = [1.0,0.15,0.3,0.5,0]
A2 = [1,0.6,0.2,0.1,0]

union = []

for i in range(len(A1)):
    union.append(max(A1[i],A2[i]))
    
print("Union: ",union)

intersection = []

for i in range(len(A1)):
    intersection.append(min(A1[i],A2[i]))
print("Intersection : ",intersection)

compliment1 = []

for i in range(len(A1)):
    compliment1.append(1-A1[i])
print("Compliment 1 : ",compliment1)

compliment2 = []

for i in range(len(A1)):
    compliment2.append(1-A2[i])
print("Compliment 2 : ",compliment2)

difference1 = []

for i in range(len(A1)):
    difference1.append(min(A1[i],compliment2[i]))
print("Difference 1 : ",difference1)

difference2 = []

for i in range(len(A1)):
    difference2.append(min(A2[i],compliment1[i]))
print("Difference 2 : ",difference2)

print("Cartesian Product :")

for i in range(len(A1)):
    print()
    for j in range(len(A2)):
        print(min(A1[i],A2[j]), )

print()

import matplotlib as plt

plt.line(A1)


