with open("inputs/day4.txt") as f:
    inp = [f.strip().split(',') for f in  f.readlines()]
    inp = [(f[0].split("-"), f[1].split("-")) for f in inp]

def isbetween(n, r1, r2):
    return r1 <= n <= r2

count = 0
for line in inp:  #1-5 2-4   2 12  1 10
    a1, a2 = int(line[0][0]), int(line[0][1])
    b1, b2 = int(line[1][0]), int(line[1][1])
    if isbetween(a1, b1, b2) or isbetween(a2, b1, b2) or isbetween(b1, a1, a2) or isbetween(b2, a1, a2):
        count += 1

print(count)