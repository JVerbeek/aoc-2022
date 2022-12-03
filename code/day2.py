with open("./2022/inputs/day2.txt") as f:
    inp = [i.strip().split(" ") for i in f.readlines()]
wins = {'A': 'B', 'B': 'C', 'C': 'A'}
losses = {v:k for (k, v) in wins.items()}
scores = {'A': 1, 'B': 2, 'C': 3}
score = 0

for i in inp: 
    if i[1] == 'X': # lose
        score += 0 + scores[losses[i[0]]]
    elif i[1] == 'Y': # draw
        score += 3 + scores[i[0]]
    else:   # loss
        score += 6 + scores[wins[i[0]]]
print(score)