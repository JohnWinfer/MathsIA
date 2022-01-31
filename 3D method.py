#Unfinished with a lot of problems


import math
import os

Height3D = 1
width3D = 0.1
stepHeight = 1
#a = 0.375
#b = -0.5
#c = 2.125
a = -1.2
b = 5.5
c = -1.33

Area2D = 387.71588
lbound = 1
ubound = 4
highestValue = 79

num = highestValue / Height3D
num = math.floor(num)

bruteforce = True
xValue = lbound
yValues3D = []
xValues3D = []
testXValue = -99999999999
while bruteforce == True:
    if round(xValue, 3) == ubound:
        bruteforce = False
        break
    yValue = a * math.pow(xValue, 2) + b * xValue + c
    yValue = round(yValue, 2)
    if yValue % stepHeight == 0 and yValue == testyValue:
        yValues3D.append(yValue)
        xValues3D.append(xValue)
    xValue = round(xValue + .0001, 10)
    testyValue = yValue

yValue = 0

duplicates = [j for n, j in enumerate(xValues3D) if j in xValues3D[:n]]

print(duplicates)

for i in range(num):
    yValue + stepHeight
    if yValue is not yValues3D:
        dist = ubound - lbound
    #elif 
    #else:



print(xValues3D)
print(yValues3D)

#for i in range(num):
    


    #height = math.sqrt(math.pow((ubound - lbound) - (i * stepHeight), 2) - math.pow(width3D / 2, 2))

    