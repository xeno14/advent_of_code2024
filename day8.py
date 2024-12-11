import collections


EXAMPLE="""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def parse(s: str):
    space = dict()
    lines = s.strip().split('\n')
    for y, line in enumerate(lines):
        for x in range(len(line)):
            if line[x] != '.':
                space[(x,y)] = line[x]

    dim = (len(line), len(lines))

    return space, dim


def visualize(space, dim):
    data = [
        ['.'] * dim[0] for _ in range(dim[1]) 
    ]

    for k, v in space.items():
        x, y = k
        data[y][x] = v

    for l in data:
        print(''.join(l))



def solve1(s: str):
    space, dim = parse(s)
    g = collections.defaultdict(list)

    for k, v in space.items():
        g[v].append(k)

    for freq, anntennas in g.items():
        for i in range(len(anntennas)):
            for j in range(len(anntennas)):
                a1 = anntennas[i]
                a2 = anntennas[j]

                dx = a2[0] - a1[0]
                dy = a2[1] - a1[1]

                b2 = (a2[0]+dx, a2[1]+dy)

                if 0 <= b2[0] < dim[0] and 0 <= b2[1] < dim[1] and space.get(b2) != freq:
                    space[b2] = '#'
    
    # visualize(space, dim)
    ans = sum(x == '#' for x in space.values())
    return ans


def solve2(s: str):
    space, dim = parse(s)
    g = collections.defaultdict(list)

    for k, v in space.items():
        g[v].append(k)

    for anntennas in g.values():
        for i in range(len(anntennas)):
            for j in range(len(anntennas)):
                if i == j:
                    continue

                a1 = anntennas[i]
                a2 = anntennas[j]

                dx = a2[0] - a1[0]
                dy = a2[1] - a1[1]

                b2 = a2
                while True:
                    b2 = (b2[0]+dx, b2[1]+dy)

                    if b2[0] < 0 or dim[0] <= b2[0] or b2[1] < 0 or dim[1] <= b2[1]:
                        break

                    if b2 not in space:
                        space[b2] = '#'
    
    # visualize(space, dim)
    ans = len(space.values())
    return ans




def main():
    print(solve1(EXAMPLE))
    print(solve2(EXAMPLE))

    with open('day8.txt') as f:
        myinput = f.read()

    print(solve1(myinput))
    print(solve2(myinput))


main()
