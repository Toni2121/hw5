import random

rnd_length = random.randint(10, 21)
print(f"Random length: {rnd_length}")

words = []

for count in range(rnd_length):
    word = ""
    word_length = random.randint(5, 20)
    for position in range(word_length):
        word += random.choice(["a", "b", "c"])
    words.append(word)

for word in words:
    print(word)
