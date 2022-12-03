import string
with open('./2022/inputs/day3.txt') as f:
    inp = [i.strip() for i in f.readlines()]

score = 0
for rucksack in inp:
    print(rucksack)
    i, j = rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]
    score += (string.ascii_lowercase + string.ascii_uppercase).index(next(iter(set(i) & set(j)))) + 1
print(score)

group_score = 0
for i in range(3, len(inp)+ 3, 3):
    group = inp[i-3:i]
    print(group)
    print(set(group[0]) & set(group[1]) & set(group[2]))
    group_score += (string.ascii_lowercase + string.ascii_uppercase).index(next(iter(set(group[0]) & set(group[1]) & set(group[2])))) + 1
print(group_score)