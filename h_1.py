with open('sample.txt', 'r') as file: #read text file and store the input as a nested list
    directions = []
    for line in file:
        numbers = list(map(int, line.strip().split()))  # Convert to integers
        directions.append(numbers)
    directions.pop()	
print(directions)

import numpy as np
arena = np.ones((11,11)) #Initiate a 11*11 grid
print(arena)

coordinates = []
for sublist in directions: #Finding the coordinates of obstacle
    x = sublist[1]-sublist[3]
    y = sublist[0]-sublist[2]
    coordinates.append([x,y])

x_coordinates = []
y_coordinates = []
for i,j in coordinates:
   x_coordinates.append(i)
   y_coordinates.append(j)
x_shift = min(x_coordinates) #Finding the x shift and y shift values to ensure that all the values fit into the list
y_shift = min(y_coordinates)

print(x_shift)
print(y_shift)

#If the shift values are non-negative, there is no need to shift 
if x_shift>=0:
   x_shift = 0
if y_shift>=0:
   y_shift = 0

#Shifting the coordinates
for i in coordinates:
    i[0] = i[0] - x_shift
    i[1] = i[1] - y_shift
print(coordinates)

#Update and print the final arena
for i in coordinates:
    a = i[0]
    b = i[1]
    arena[b][a] = 0
print(arena)
        
