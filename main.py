
import math
import os

os.system('cls' if os.name == 'nt' else 'clear')

passC = 0

while True:
    error = True

    if passC == 5:
        print("Please insert 3D step width:")
        width3D = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            width3D = float(width3D)
            error = False
        except:
            print("Invalid Input")
            error = True

    if passC == 4:
        passC = 5
        print("Please insert step length:")
        sLength = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            sLength = float(sLength)
        except:
            passC = 4
            print("Invalid Input")

    
    if passC == 3:
        passC = 4
        print("Please insert upperbound:")
        uBound = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            uBound = float(uBound)
        except:
            print("Invalid Input")
            passc = 3

    if passC == 2:
        passC = 3
        print("Please insert lowerbound:")
        lBound = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            lBound = float(lBound)
        except:
            print("Invalid Input")
            passC = 2
            
    if passC == 1:
        passC = 2
        print("Please insert Y values seperated by commas:")
        userInput = input()
        y = userInput.split(",")
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(0, len(y)):
            try:
                y[i] = float(y[i])
            except:
                print("Invalid Input")
                passC = 1

    
    if passC == 0 : 
        passC = 1
        print("Please insert X values seperated by commas:")
        userInput = input()
        x = userInput.split(",")
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(0, len(x)):
            try:
                x[i] = float(x[i])
            except:
                print("Invalid Input")
                passC = 0
   
#---------------------------------------------------------------------------------------------------------------------
#Approximating the quadratic curve 

    aMatrix = []
    xMatrix = []
    
    if error == False: #If all inputs are valid, proceed with calculations
        num = 0

        for expon in range(5): #Create the X matrix
            num = 0
            for i in x:
                num = num + math.pow(i, expon)
            xMatrix.append(round(num, 10))

        num = 0
        num1 = 0
        count = 0

        for i in x: #Create Y matrix
            num = num + math.pow(i, 2) * y[count] 
            num1 = num1 + i * y[count]
            count = count + 1

        aMatrix.extend((round(num, 10), round(num1, 10), round(sum(y), 10))) 

        num = 0
        for i in range(2):
            xMatrix.append(round(xMatrix[i + 2] - (xMatrix[1] / xMatrix[2]) * xMatrix[i + 3], 10)) #Calculate Second Row

        aMatrix[1] = round(aMatrix[1] - (xMatrix[1] / xMatrix[2]) * aMatrix[0], 10)
                

        #Find values using substition
        a = (round((aMatrix[2] - (xMatrix[0]/xMatrix[2]) * aMatrix[0]) - ((xMatrix[1] - (xMatrix[0] / xMatrix[2]) * xMatrix[3]) / xMatrix[5]) * aMatrix[1], 10)) / round((xMatrix[2] - (xMatrix[0]/xMatrix[2]) * xMatrix[4]) - ((xMatrix[1] - (xMatrix[0] / xMatrix[2]) * xMatrix[3]) / xMatrix[5]) * xMatrix[6], 10) #Calculate 3rd Row 
        b = (aMatrix[1] - a * xMatrix[6]) / xMatrix[5]
        c = (aMatrix[0] - (xMatrix[4] * a) - (xMatrix[3] * b)) / xMatrix[2]
        
#---------------------------------------------------------------------------------------------------------------------
#2D Area:

        dist = (uBound - lBound) / sLength

        try:
            dist = int(dist)
            extra = 0

        except:
            extra = round(dist % 1, 10) 
            math.ceil(dist)
            dist = int(dist)

        
        dist1 = dist + sLength
        num = 0
        xn = lBound + sLength
        for i in range(dist - 2):
            num = num + a*math.pow(xn, 2) + b * xn + c
            xn = xn + sLength
        highestValue = max(a*math.pow(lBound, 2) + b * lBound + c, a*math.pow(uBound, 2) + b * uBound + c)
        area2D = 0.5 * (sLength*((a*math.pow(lBound, 2) + b * lBound + c) + (a*math.pow(uBound, 2) + b * uBound + c) + (2 * num)))
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Quadratic Equation is:", round(a, 5),"x^2 +",round(b, 5),"x +",round(c, 5))
        print ("2D area under the shape is:", round(area2D,5), "m^2")

#---------------------------------------------------------------------------------------------------------------------
#3D Area:

        dist = dist * sLength
        remover = (((dist * highestValue) - area2D) * width3D) / 2 
        height = math.sqrt(math.pow(dist, 2) - math.pow(width3D / 2, 2))
        angle = (math.asin((width3D / 2) * (math.sin(90) / dist))) * 2
        num = ((width3D * height) / 2) * highestValue
        segment = num - remover
        angle = 360 / angle
        area3D = angle * segment
        print("Revolved 3D volume is:", round(area3D, 5), "m^3")

        passC = 0
        asas = input()
        os.system('cls' if os.name == 'nt' else 'clear')




