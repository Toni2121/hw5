import random

length = random.randint(5,21)
word = ""
for count in range(random.randint(5, 21)):
    rnd_letters: str = random.choice(["a", "b", "c"])
    word += rnd_letters
print(word)
word: list[str] = []
word.append(rnd_letters)
print(word)
