number = int(input("Please enter a number larger than 0: "))
if number > 0:
    for i in range(1, number + 1, 2):

        height = (number - i) // 2
        for j in range(height):
            print(" ", end="")
        for j in range(1, i + 1):
            print("*", end="")
        print()
else:
    print("The number you've entered is smaller than 0.")
