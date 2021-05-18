#importing modules
import random

#Ask user for password length
passlen = int(input("Enter password lenght : "))

#Set possible characters
bowl ="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?,./<>:':"

#Create random password and display in a nice way
passwd = "".join(random.sample(bowl,passlen ))
print("Generated Password : ",passwd)