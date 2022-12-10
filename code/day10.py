with open("inputs/day10.txt") as f:
    inp = [i.strip().split(" ") for i in f.readlines()]

def crt(pixels, cycle, X):
    if X - 1 <= cycle % 40 <= X + 1:
        pixels += "#"
    else:
        pixels += "."
    return pixels 

cyclelength = {"noop": 1, "addx": 2}
X = 1
we_at = 0
pixels = ""
for line in inp: 
    cycle = cyclelength[line[0]]
    for i in range(cycle):
        we_at += 1
        pixels = crt(pixels, we_at-1, X)
        if we_at in range(0, 320, 40):
            print(pixels)
            pixels = ""
        if i == 0:
            continue
        else:
            X += int(line[1])
        
    


    
  