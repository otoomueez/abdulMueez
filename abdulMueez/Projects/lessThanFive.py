# Assign list of integers to var a
a = [1, 2, 3, 5, 8, 13, 21, 4, 0, 89]

b = []
[b.append(i) for i in a if i < 5]
print(b)