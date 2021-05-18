names = ["Kwame", "Stephen", "Ama", "Esi"]

length = map(len, names)

print(length)

lengths = [3,5,6,8,9]

def sqr(x): return x**2

# square = map(sqr, lenghts)
# sqrlengths = map(sqr, names)
lengths = map(len, names)
sqrlength = map(sqr, length)
sqrlens = map((lambda x : x**3), length)


# print(*sqrlengths)
print(*sqrlens)
print(*sqrlength)


ages = [26, 15, 19, 39, 25]

def can_vote(x): x > 17
voters = filter(can_vote, ages)
print(*voters)