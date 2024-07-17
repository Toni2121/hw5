pos_num: int = 0
neg_num: int = 0
div_7: int = 0
last_pos: int = None
last_neg: int = None

for _ in range(1, 11):
    num: int = int(input("please enter a number: "))
    if -1000 > num > 1000:
        continue
    if num == -9999:
        break
    if num > 0:
        pos_num += 1
        last_pos = num
    elif num < 0:
        neg_num += 1
        last_neg = num

    if num % 7 == 0:
        div_7 += 1
else:
    print(f"amount of positives: {pos_num}")
    print(f"amount of negatives: {neg_num}")
    print(f"amount of numbers divisible by 7: {div_7}")
    if last_pos is not None:
        print(f"last positive number: {last_pos}")
    else:
        print("positive numbers: None")
    if last_neg is not None:
        print(f"last negative number: {last_neg}")
    else:
        print("negative numbers: None")
