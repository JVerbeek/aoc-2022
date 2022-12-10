import copy
import sys
with open("inputs/day9.txt") as f:
    inp = [i.strip().split(" ") for i in f.readlines()]

def move(end, dir):
    if dir == "L":
        end[1] += -1
    elif dir == "R":
        end[1] += 1
    elif dir == "U":
        end[0] += 1
    else:  # DOWN
        end[0] += -1
    return end

def tail_iftree(head, tail):
    counter = []
    # are the head and tail touching or diagonal
    ycoord = head[0] - tail[0] 
    xcoord = head[1] - tail[1]
    if (abs(xcoord) == 2 and abs(ycoord) == 0) or (abs(xcoord) == 0 and abs(ycoord) == 2):    
        if ycoord == 0 and xcoord == 2:   # head is right of tail
            tail = move(tail, "R")
        elif ycoord == 0 and xcoord == -2:
            tail = move(tail, "L")
        elif ycoord == -2 and xcoord == 0:
            tail = move(tail, "D")
        else: 
            tail = move(tail, "U")
        return tail, [tuple(tail)]

    elif (abs(xcoord) == 2 and abs(ycoord) == 1) or abs(xcoord) == 1 and abs(ycoord) == 2:   # different row and col, diagonal move
        moves = []
        if ycoord < 0:
            tail = move(tail, "D")
            if xcoord < 0:
                tail = move(tail, "L")
            else:
                tail = move(tail, "R")
        else:
            tail = move(tail, "U")
            if xcoord < 0:
                tail = move(tail, "L")
            else:
                tail = move(tail, "R")
        moves.append(tuple(tail))
        return tail, moves
    return tail, [tuple(tail)]


head = [0, 0]   # row, col   
tail = [0, 0]

tail_pos_counter = []
for ind, i in enumerate(inp):  # (assume start (0, 0); l = -1, r = 1 ; u = 1, d = -1)
    # Move the head
    dir, mag = i[0], int(i[1])
    for j in range(mag):
        head = move(head, dir)
        tail, moves = tail_iftree(head, tail)
        tail_pos_counter.append(moves)
print(head, tail)
tail_pos_counter = [pos[0] for pos in tail_pos_counter]
print(len(set(tail_pos_counter)))


# I do knot want to do this
knots = [[0, 0] for i in range(10)]
tail_pos_counter = []

for ind, i in enumerate(inp):  # (assume start (0, 0); l = -1, r = 1 ; u = 1, d = -1)
    # Move the head
    dir, mag = i[0], int(i[1])
    for j in range(mag):
        knots[0] = move(knots[0], dir)
        print(knots)
        for i in range(1, len(knots)):
            knots[i], moves = tail_iftree(knots[i-1], knots[i])
            if i == 9:
                tail_pos_counter.append(moves)
print(knots[0], knots[9])
tail_pos_counter = [pos[0] for pos in tail_pos_counter]
print(len(set(tail_pos_counter)))