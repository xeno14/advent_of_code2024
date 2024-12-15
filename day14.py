import re


EXAMPLE="""
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


def parse(s:str):
    for line in s.strip().split('\n'):
        yield tuple(map(int, re.findall(r'(\-?[0-9]+)', line)))


def evolution(init_conditions, t, dimx, dimy):
    locs = []
    for x, y, vx, vy in init_conditions:
        x = (x + vx * t) % dimx
        y = (y + vy * t) % dimy
        locs.append((x, y))

    return locs


def solve1(s:str, dimx, dimy):
    locs = evolution(parse(s), 100, dimx, dimy)
    count1=0 
    count2=0 
    count3=0 
    count4=0 
    for x, y in locs:
        x0 = x < dimx // 2
        y0 = y < dimy // 2
        x1 = x > dimx // 2
        y1 = y > dimy // 2

        count1 += (x0 and y0)
        count2 += (x0 and y1)
        count3 += (x1 and y0)
        count4 += (x1 and y1)

    return count1 * count2 * count3 * count4


def visualize(locs, dim):
    data = [
        ['.'] * dim[0] for _ in range(dim[1]) 
    ]

    for loc in locs:
        x, y = loc
        data[y][x] = '1'

    lines = [''.join(l) for l in data]
    return '\n'.join(lines)



def solve2(s:str,dimx=101, dimy=103):
    ini = list(tuple(parse(s)))

    for t in range(1, 10000001):
        locs = evolution(ini, t, dimx, dimy)
        pic = visualize(locs, (dimx, dimy))
        if '1111111111' in pic:
            print(pic)
            return t
        t += 1
    raise RuntimeError('Tree not found')



def main():
    print(solve1(EXAMPLE, dimx=11, dimy=7))

    with open('day14.txt') as f:
        my_input = f.read()

    print(solve1(my_input, dimx=101, dimy=103))

    print(solve2(my_input))


main()
