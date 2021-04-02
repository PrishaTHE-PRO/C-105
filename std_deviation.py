import csv
import math
with open('Data.csv',newline='') as f :
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#step 1 finding mean
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total += int(x)
        #total = int(total+x)
    #total+=x
    mean=total/n
    return mean

#step 2 squaring and getting the values
squared_list=[]
for number in data:
    a=int(number) - mean(data)
    a=a**2
    squared_list.append(a)

#step 3 getting sum
sum=0
for i in squared_list:
    sum=sum+i

#step 4 dividing the sum by the total value
result=sum/(len(data)-1)

#step 5 getting the standard deviation by taking the square root of the result
sd=math.sqrt(result)
print('standard deviation is =>',sd)