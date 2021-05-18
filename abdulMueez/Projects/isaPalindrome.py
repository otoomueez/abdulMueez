#Ask user for input
word = str(input("Enter text for check : "))

#Slice word and return result
def isPalindrome(word):
    word = word.lower()
    return word == word[::-1]
 
 
# Condition to check and print result
wdPal = isPalindrome(word)
 
if wdPal:
    print("Yes")
else:
    print("No")

