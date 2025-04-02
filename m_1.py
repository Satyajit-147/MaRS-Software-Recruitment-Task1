#Initial rover position
x_reference = int(input('Initial x-coordinate: ')) 
y_reference = int(input('Initial y-coordinate: '))
z_reference = int(input('Initial z-coordinate: '))

print(f'Intial frame of reference: ({x_reference},{y_reference},{z_reference})')
#Final rover position
x_moved = int(input('Final x-position before correction: '))
y_moved = int(input('Final y-position before correction: '))
z_moved = -60

#Printing the position of the rover before correction
print(f'Position of rover before correction: ({x_moved},{y_moved},{z_moved})')

#Function to calculate the distance moved by the rover
def caldist(x,y,z,x_m,y_m,z_m):
     dist = (((x_m-x)**2)+((y_m-y)**2)+((z_m-z)**2))**0.5
     return dist


distance = caldist(x_reference,y_reference,z_reference,x_moved,y_moved,z_moved)

#Function to correct the coordinates
def adjusted_coordinates(x,y,z,x_m,y_m,z_m,distance):
	
    #Unit vector
    x_unit = (x_m-x)/(distance)
    y_unit = (y_m-y)/(distance)
    z_unit = (z_m-z)/(distance)

    x_adjusted = x_m + x_unit*55
    y_adjusted = y_m + y_unit*55
    z_adjusted = z_m + z_unit*55

    #Printing the adjusted coordinates
    print(f'Adjusted coordinates: ({x_adjusted},{y_adjusted},{z_adjusted})')
    
adjusted_coordinates(x_reference,y_reference,z_reference,x_moved,y_moved,z_moved,distance)



