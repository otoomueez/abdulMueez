#for i in range(1,11):
 #   print(i)


def gen_list():
    return[x for x in range (0, 20) if x % 2 == 0 ]

print(gen_list())


# Function  to produce and output
length = 1
for i in range(0,8):
    print("*" * length)
    if (i >= 3):
        length -= 1
    else:
        length += 1
