import random

songs: list[str] = ["If we being real", "Type shit", "Flawless"]
songs.append("Like that")
songs.insert(0, "Freestyle")
print(songs)
print(len(songs))


num: list[int] = []
for rnd_num in range(1,11):
    rnd_num: int = random.randint(1, 100)
    num.append(rnd_num)
print(num)


bool1: list[bool] = []
for rnd_bool in range(1,11):
    rnd_bool: bool = random.choice([False, True])
    bool1.append(rnd_bool)
print(bool1)