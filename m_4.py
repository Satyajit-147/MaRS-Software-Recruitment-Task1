n = int(input('Number of sensor readings: '))
Data = []
for i in range(n): #Input sensor readings
    reading = int(input())
    Data.append(reading)
print(Data)
windowsize = int(input('Enter the size of the window: ')) #Input window size
sublist_len = n-windowsize+1 
output = []
output2 = []

def Muchiko():
    for j in range(windowsize): 
            templis = Data[j:j+sublist_len]  #Slicing done to the length of sublist which was calculated earlier
            average = sum(templis) / len(templis)
            output.append(average)
    return output

def Sanchiko():
    for k in range(windowsize): 
            templis2 = sorted(Data[k:k+sublist_len]) #Slicing followed by sorting to calculate the medin
            if len(templis2)%2!=0:
                median = templis2[len(templis2)//2] #median formula if the number of elements in the list is odd
            else:
                median = (templis2[len(templis2)//2 - 1] + templis2[len(templis2)//2])/2 #median formula if the number of elements in the list is even
            output2.append(median)           
    return output2

a = Muchiko()
b = Sanchiko()

print('Muchiko Filter: ',a)
print('Sanchiko Filter: ',b)
import statistics

#calculate the standard deviation of two different lists
sd_a = statistics.stdev(a) 
sd_b = statistics.stdev(b)

#Compare the two lists and print the result
if sd_a<sd_b:
     print('Muchiko filter is the best for the given sensor readings and window size')
elif sd_a>sd_b:
     print('Sanchiko filter is the best for the given sensor readings and window size')
