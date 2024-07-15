
from matplotlib import pyplot as plt

file = "WeatherDataCLL.csv"
with open (file,"r") as file:
     datas = file.read().split('\n')
     
print(datas)

count=1
wSpd=[]
prcp=[]
aTemp=[]
maxTemp=[]
minTemp=[]
date=[]

while True:
    #chekcing to make sure it is not out of bounds
    if count >=len(datas)-1:
        break
    #splitting each line into a list
    line=datas[count]
    lineList=line.split(',')
    #taking the index of the values in the list, and appending them into correct value lists. 
    date.append(lineList[0])
    wSpd.append(float(lineList[1]))
    prcp.append(float(lineList[2]))
    aTemp.append(int(lineList[3]))
    maxTemp.append(int(lineList[4]))
    minTemp.append(int(lineList[5]))
    #the count increases by one
    count+=1
    
#plot 1
plt.figure
plt.plot(date,maxTemp,'r')
plt.xlabel('date')  
plt.ylabel('Maximum temperature, F') 
plt.legend(['Max Temp'])
plt.twinx().plot(date, wSpd, 'b')
plt.ylabel('Average Wind speed, mph')
plt.legend(['Avg Wind'])
plt.title('Maximum Temperature and Average Wind Speed')
plt.show()
    

#plot 2
plt.figure
hist = plt.hist(wSpd, 30, color= 'green', edgecolor = 'black')
plt.xlabel("Average Wind Speed, mph")
plt.ylabel("Number of Days")
plt.title("Histogram of average wind speed")

plt.axis()
plt.show()
    
#plot 3
plt.figure
plt.xlabel('Minimum Temperature, F')  
plt.ylabel("Average Wind Speed, mph") 
plt.title("Average Wind Speed vs Minimum Temperature")
plt.scatter(minTemp, wSpd, s=8,color = 'black')
plt.show()
   
''' 
#4
plt.figure
month = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.xlabel("Month")
plt.ylabel("Average Temperature, F")
plt.title("Temperature by Month")
plt.bar(month)
    
    '''
    
    
