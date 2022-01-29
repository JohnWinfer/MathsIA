import math
import os

x = [1,3,5,7,9,11,13,15]
y = [60,35.2,16.7,10.93,7.12,4.45,2.05,0]
aMatrix = []
xMatrix = []
row2 = []

row3 = []
num = 0

for expon in range(5):
    num = 0
    for i in x:
        num = num + math.pow(i, expon)
    xMatrix.append(round(num, 10))

num = 0
num1 = 0
count = 0

for i in x:
    num = num + math.pow(i, 2) * y[count] #need to find a diffrent way to do this.
    num1 = num1 + i * y[count]
    count = count + 1

aMatrix.extend((round(num, 10), round(num1, 10), round(sum(y), 10))) 

num = 0
for i in range(2):
    xMatrix.append(round(xMatrix[i + 2] - (xMatrix[1] / xMatrix[2]) * xMatrix[i + 3], 10))

aMatrix[1] = round(aMatrix[1] - (xMatrix[1] / xMatrix[2]) * aMatrix[0], 10)
           
print(xMatrix)

print (aMatrix)

a = (round((aMatrix[2] - (xMatrix[0]/xMatrix[2]) * aMatrix[0]) - ((xMatrix[1] - (xMatrix[0] / xMatrix[2]) * xMatrix[3]) / xMatrix[5]) * aMatrix[1], 10)) / round((xMatrix[2] - (xMatrix[0]/xMatrix[2]) * xMatrix[4]) - ((xMatrix[1] - (xMatrix[0] / xMatrix[2]) * xMatrix[3]) / xMatrix[5]) * xMatrix[6], 10)
b = (aMatrix[1] - a * xMatrix[6]) / xMatrix[5]
c = (aMatrix[0] - (xMatrix[4] * a) - (xMatrix[3] * b)) / xMatrix[2]
print(a)
print(b)
print(c)

