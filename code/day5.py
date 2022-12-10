import re
with open("inputs/day5test.txt") as f:
    inp = f.readlines()

boxes = [[] for i in range(3)]

for line in inp:
    for i in range(len(line)):
        if line[i].isupper():
            letter, xind = line[i], int((i+3)/4)
            boxes[xind-1].append(letter)
    m = re.search("\d+ from \d to \d", line)
    if m:  # beginning of array is top box
        instruction = m.group(0).split(" ")
        amount, fr, to = int(instruction[0]), int(instruction[2]), int(instruction[4])
        boxes[to-1] = boxes[fr-1][:amount] + boxes[to-1]  # take amount boxes from beginning of array, reverse
        boxes[fr-1] = boxes[fr-1][amount:]
        print(boxes)
print("".join([box[0] for box in boxes]))