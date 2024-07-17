number: int = int(input("please enter a number larger then 0: "))
if number > 0:
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

    for i in range(number - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

else:
    print("the number you've entered is smaller then 0.")