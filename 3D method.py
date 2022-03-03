#Unfinished but we're makeing progress

import math
import os
from turtle import width

from numpy import angle



angle3D = 0.1
stepHeight = 0.5
a = 0.375
b = -0.5
c = 2.125
#a = -1.2
#b = 5.5
#c = -1.33

Area2D = 387.71588
lbound = 1
ubound = 5





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
    if yValue % stepHeight == 0 and yValue != testyValue and yValue >= 0:
        yValues3D.append(yValue)
        xValues3D.append(xValue)
    xValue = round(xValue + .0001, 10)
    testyValue = yValue 

testList = []
duplicates = []
for i in yValues3D:
    if (i in testList):
        duplicates.append(i)
    else:
        testList.append(i)


yValue = 0
total = 0
waitingList = []
waitingListY = []

angle3D = angle3D / 2
fltrigA = min(yValues3D) / stepHeight

height = ubound - lbound

angleB = 90 - angle3D

width = height * (math.sin(angle3D * 0.01745) / math.sin(angleB * 0.01745))
fltrig = ((height * width) / 2) * stepHeight
total = fltrig * fltrigA
count = 0
print(total)
for i in xValues3D:
    height = i - lbound
    width =  height * (math.sin(angle3D * 0.01745) / math.sin(angleB * 0.01745))
    trig = (((width * height) / 2) * stepHeight)
    if yValues3D[count] in duplicates:
        if yValues3D[count] in waitingListY:
            count1 = 0
            for z in waitingListY:
                if z == yValues3D[count]:
                    saved = count1
                    break
                else:
                    count1 = count1 + 1
            if a >= 0:
                trig = fltrig - (trig - waitingList[saved])
            else:
                trig = trig - waitingList[saved]
        else:
            waitingList.append(trig)
            waitingListY.append(yValues3D[count])
    
    total = total + trig
    count = count + 1
total = total * (360 / angle3D)


print(total)

print(xValues3D)
print(yValues3D)
print(duplicates)



#Notes:
# duplicates get subtraceted from each other
# if yvalue is not on list, take lbound and upound 
