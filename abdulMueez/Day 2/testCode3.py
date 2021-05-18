import math

#Convert degrees to radians
pi = 22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

#Ask user for radius then prints out the surface area and volume of a sphere
pi = 22/7
radius = float(input("Input radius: "))
area = 4*pi*(radius**2)
volume = 4*pi*((radius**3)/3)
print("Surface area is ", area)
print("Volume is ", volume)

#Tell the time of the day
import datetime
now = datetime.datetime.now()
print ("Current time : ")
print (now.strftime("%H:%M:%S"))

#Split a sentence into its words

