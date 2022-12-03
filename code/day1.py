import os
import numpy as np

print(os.getcwd())
with open("2022/inputs/day1.txt") as f:
    input = f.readlines()
stripped = [sum(np.array(j.split(' ')).astype(int)) for j in " ".join([i.strip() for i in input]).split("  ")]

print(sum(np.sort(stripped)[-3:]))