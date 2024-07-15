
import numpy as np
from matplotlib import pyplot as plt
#a = np.arange(4).reshape(2,2)

#making a matrix with the given values
matrix = np.array([[1.01,.09],[-.09,1.01]])
point = np.array([[0],[1]])


pointsList = [] #creating a list that stores the values of th
pointsList.append(point) #adding the starting point to the list

for i in range (200): #loops 200 times
    point = matrix @ point #multiplyingold point with the matrix to get the new point
    pointsList.append(point) #adding the point to the list
  
    
xPoints,yPoints = zip(*pointsList)
plt.scatter(xPoints,yPoints) #Plotting the x and y points
plt.xlabel("x-axis") #labeling x axis
plt.ylabel("y-axis") #labeling y axis
plt.suptitle("Swirl") #title of the graph
plt.show() #showing the graph