#Unfinished but we're making progress

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
ubound = 15
highestValue = 79

num = highestValue / Height3D
num = math.floor(num)

bruteforce = True
xValue = lbound
yValues3D = []
xValues3D = []
testyValue = None
while bruteforce == True:
    if round(xValue, 3) == ubound:
        bruteforce = False
        break
    yValue = a * math.pow(xValue, 2) + b * xValue + c
    yValue = round(yValue, 3)
    if yValue % stepHeight == 0 and yValue != testyValue:
        yValues3D.append(yValue)
        xValues3D.append(xValue)
    xValue = round(xValue + .0001, 10)
    testyValue = yValue #This loop is so stupid but it works

testList = []
duplicates = []
for i in yValues3D:
    if (i in testList):
        duplicates.append(i)
    else:
        testList.append(i)


yValue = 0


for i in range(num):
    yValue + stepHeight
    if yValue is not yValues3D:
        dist = ubound - lbound
    else:
        dist = xValue - lbound
    height = math.sqrt(math.pow((dist), 2) - math.pow(width3D / 2, 2))


print(xValues3D)
print(yValues3D)
print(duplicates)


#Notes:
# duplicates get subtraceted from each other
# if yvalue is not on list, take lbound and upound 

####################

import math
import os

Height3D = 1
width3D = 0.1
stepHeight = 1
a = 0.375
b = -0.5
c = 2.125
#a = -1.2
#b = 5.5
#c = -1.33

Area2D = 387.71588
lbound = 1
ubound = 14
highestValue = 79

num = highestValue / Height3D
num = math.floor(num)

bruteforce = True
xValue = lbound
yValues3D = []
xValues3D = []
testyValue = None
while bruteforce == True:
    if round(xValue, 3) == ubound:
        bruteforce = False
        break
    yValue = a * math.pow(xValue, 2) + b * xValue + c
    yValue = round(yValue, 3)
    if yValue % stepHeight == 0 and yValue != testyValue:
        yValues3D.append(yValue)
        xValues3D.append(xValue)
    xValue = round(xValue + .0001, 10)
    testyValue = yValue #This loop is so stupid but it works

testList = []
duplicates = []
for i in yValues3D:
    if (i in testList):
        duplicates.appensd(i)
    else:
        testList.append(i)
print(yValues3D)

yValue = 0

angle = (math.asin((width3D / 2) * (math.sin(90) / ubound - lbound)))

segmentList = []

count = 0

for i in range(num):
    if yValue not in yValues3D:
        dist = ubound - lbound
        print("dupe")
    else:
        count = count + 1
        dist = xValues3D[count] - lbound
        print("yValue")
        print(yValue)
        print("XValue")
        print(xValues3D[count])
        print("Dist")
        print(dist)
    height = dist * (math.sin(90) / math.sin(180 - (90 + angle)))
    width = math.sqrt(math.pow(dist, 2) - math.pow(height, 2))
    triarea = ((width * height) / 2)
    segmentList.append(triarea * stepHeight)
    print(segmentList)
    yValue = yValue + stepHeight
    yValue = float(yValue)


print(xValues3D)
print(yValues3D)
print(duplicates)
print(segmentList)
print(yValue)
