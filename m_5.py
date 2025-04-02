#Input the nagle made with x-axis(alpha), y-axis(beta) and z-axis(gamma)
theta_x = int(input('Rotation angle with x-axis: '))
theta_y = int(input('Rotation angle with y-axis: '))
theta_z = int(input('Rotation angle with z-axis: '))

import math
def numsystem_converter():
    #convert the angles to radians and then calculate the half angle
    theta_x1 = math.radians(theta_x) / 2  
    theta_y1 = math.radians(theta_y) / 2  
    theta_z1 = math.radians(theta_z) / 2

    #Convert 3-number system to 4-number system
    w = math.cos(theta_x1)*math.cos(theta_y1)*math.cos(theta_z1) + math.sin(theta_x1)*math.sin(theta_y1)*math.sin(theta_z1)
    x = math.sin(theta_x1)*math.cos(theta_y1)*math.cos(theta_z1) - math.cos(theta_x1)*math.sin(theta_y1)*math.sin(theta_z1)
    y = math.cos(theta_x1)*math.sin(theta_y1)*math.cos(theta_z1) + math.sin(theta_x1)*math.cos(theta_y1)*math.sin(theta_z1)
    z = math.cos(theta_x1)*math.cos(theta_y1)*math.sin(theta_z1) - math.sin(theta_x1)*math.sin(theta_y1)*math.cos(theta_z1)

    #Rounding off the final result and printing the values
    print('4-number system representations: ',round(w,4),round(x,4),round(y,4),round(z,4))

numsystem_converter()

