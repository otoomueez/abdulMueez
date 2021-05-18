i = 0
while(i < 10):
    i = i + 1
    print (i)

# i is initially assigned to 0
# From the condition stated in the while loop statement,
# the code continues to run if and only if the i is less than 10
# and after each process or loop, i is increased by 1.
# The numbers 7 to 10 can be printed but 11 to 19 cant be printed
# under the condition stated.
# Though 10 is greater than i, it'll be printed because the 
# increment happens and prints before the next loop.

# Numbers between 12 and 20 cannot be printed

# Function evens that takes two numbers and prints evens between them


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def evens():
    return[x for x in range(num1 + 1, num2 + 1) if x % 2 == 0]

print(evens())

# Print even numbers in reverse

def reverse(evens):
    return[y for y in reverse(evens)]
#reverse_evens() = evens.reverse()
print(reverse())