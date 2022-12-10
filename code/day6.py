import string
with open("inputs/day6.txt") as f:
    inp = f.readline()
n_unique = 14
chars = set()
for i in range(n_unique, len(inp)):
    window = inp[i-n_unique:i]
    if len(set(window)) == n_unique:
        print(i)
        break
print("finished")