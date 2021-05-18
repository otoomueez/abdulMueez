#importing modules
import string

#Ask user for phrase and print output
# words = input("Enter a phrase or concept : ").upper().split()
# for word in words:
#     print(word[0], end = "")


words = input("Enter a phrase or concept : ")
words = words.upper()
w_list = words.split()
for word in w_list:
    print(word[0], end = "" )