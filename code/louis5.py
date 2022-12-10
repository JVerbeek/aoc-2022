t = ['ZN', 'MCD', 'P']
i = ['CZNBMWQV', 'HZRWCB', 'FQRJ', 'ZSWHFNMT', 'GFWLNPQ', 'LPW', 'VBDRGCQJ', 'ZQNBW', 'HLFCGTJ']

stacks = i

with open(f'i2.txt', 'r') as file:
    for line in file:
        parts = line.split(' ')
        parts = [int(x.rstrip('\n')) for x in [parts[1], parts[3], parts[5]]]

        print(parts)
        origin = stacks[parts[1] - 1]
        dest = stacks[parts[2] - 1]
        cargo = origin[(parts[0] * -1):][::-1]
        stacks[parts[1] - 1] = origin[:parts[0] * -1]
        stacks[parts[2] - 1] = dest + cargo

        print(stacks)

    part1 = ''
    for n in stacks:
        part1 += n[-1]
    print(part1)