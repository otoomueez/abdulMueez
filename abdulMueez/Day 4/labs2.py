# def function returning even numbers
numbers = [1,56,234,87,4,76,24,69,90,135]
def is_even(x): return x % 2 == 0
result = filter(is_even, numbers)
print(is_even(4))
print(*result)

# def function returning even and odd numbers numbers
numbers = [1,56,234,87,4,76,24,69,90,135]
# def is_even(x): return x % 2 == 0

# Using lambda
even_result = filter((lambda x : x %2 == 0), numbers)
odd_result = filter((lambda x : x %2 == 1), numbers)
# print(is_even(4))
print(*even_result)
print(*odd_result)

# Combinations
def is_even(numbers):
    return [a for a in numbers if not a %2 == 0]
print(is_even(numbers))

# FOLD
from functools import reduce

words = ["hello"," world", " isis", " ha"]
def join_string(data): 
    print(reduce((lambda x, y : x + '' + y), data))
join_string(words)

#LIST COMPREHENSIONS

# Function to print only positive numbers
numbers1 = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
def pos_nums(numbers1) : return [a for a in numbers1 if a > 0]
print(pos_nums(numbers1))

# Function to print only positive numbers
numbers2 = [12, 54, 33, 67, 24, 89, 11, 24, 47]
def even_nums(numbers2) : return [a for a in numbers2 if a %2 == 0]
print(even_nums(numbers2))

# Return upper case letters and its length
words = ["hello", "my", "name", "is", "Sam"]

# length = map(len, words)
length = len(words)
u_words = (words[0].upper())
print(u_words, length)


