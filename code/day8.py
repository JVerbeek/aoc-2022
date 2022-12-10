import numpy as np

with open("inputs/day8.txt") as f:
    inp = np.array([" ".join(i.strip()).split(" ") for i in f.readlines()]).astype(int)

count = inp.shape[0] * 2 + (inp.shape[1] - 2) * 2
print(count)

for i in range(0, inp.shape[0]-1):
    for j in range(0, inp.shape[1]-1):
        if i == 0 or i == inp.shape[0] or j == 0 or j == inp.shape[1]:
            continue
        else: 
            tree = inp[i, j]
            horz = inp[i,:]
            vert = inp[:,j]

            if (tree > horz[:j]).all() or (tree > horz[j+1:]).all() or (tree > vert[:i]).all() or (tree > vert[i+1:]).all():
                count += 1

def viz(tree, arr, is_reverse=False):    # ew ew ew ew ew 
    score = 0
    if is_reverse:
        arr = arr[::-1]
    for a in arr:
        if a < tree:
            score += 1
        else:
            score += 1
            break
    return score

# More loop, whatever
scores = np.zeros(inp.shape)
for i in range(0, inp.shape[0]-1):
    for j in range(0, inp.shape[1]-1):
        if i == 0 or i == inp.shape[0] or j == 0 or j == inp.shape[1]:
            continue
        else:
            tree = inp[i, j]
            tras = [viz(tree, inp[i,:j], True), viz(tree, inp[i,j+1:]), viz(tree, inp[:i,j], True), viz(tree, inp[i+1:,j])] #lrud
            scores[i, j] = np.prod(tras)
print(scores.max(), "viz score")
print(count)
    