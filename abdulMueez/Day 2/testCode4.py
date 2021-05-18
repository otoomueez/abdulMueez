def stars2():
    a = [1,2,3,4,5,6,7]

    for i in a:
        if i < 5:
            for j in range(i):
                print("*", end="")
            print("")
        else:
            for j in range(a[-i]):
                print("*", end="")
            print("")

stars2()
