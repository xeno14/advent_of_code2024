EXAMPLE="""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

EXAMPLE_LOOP="""
....#.....
.........#
..........
..#.......
.......#..
..........
.#.#^.....
........#.
#.........
......#...
"""


def parse(s: str):
    lines = s.strip().split('\n')
    guards = set()
    start = (-1, -1)
    for y, line in enumerate(lines):
        for x in range(len(line)):
            if line[x] == '#':
                guards.add((x, y))
            elif line[x] == '^':
                start = (x, y)


    dim = (len(line), len(lines))

    return start, guards, dim


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
DIRECTION = (
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
)

def visualize(locs, dim):
    data = [
        ['.'] * dim[0] for _ in range(dim[1]) 
    ]

    for loc in locs:
        x, y = loc
        data[y][x] = 'X'

    for l in data:
        print(''.join(l))


def solve1(s:str):
    start, guards, dim = parse(s)

    dir = UP
    pos = start
    visited = set()
    while 0 <= pos[0] < dim[0] and 0 <= pos[1] < dim[1]:
        visited.add(pos)
        vel = DIRECTION[dir]
        npos = (pos[0] + vel[0], pos[1] + vel[1])
        if npos in guards:
            dir = (dir + 1) % 4
        else:
            pos = npos

    # visualize(visited, dim)
    return len(visited)


def is_loop(start, guards, dim):
    dir = UP
    pos = start
    visited = set()
    while 0 <= pos[0] < dim[0] and 0 <= pos[1] < dim[1]:
        if (pos, dir) in visited:
            return True
        visited.add((pos, dir))
        vel = DIRECTION[dir]
        npos = (pos[0] + vel[0], pos[1] + vel[1])
        if npos in guards:
            dir = (dir + 1) % 4
        else:
            pos = npos
    return False


def solve2(s:str):
    start, guards, dim = parse(s)

    ans = 0
    for x in range(dim[0]):
        print('X: %d/%d' % (x+1, dim[0]))
        for y in range(dim[1]):

            pos = (x, y)
            if pos in guards:
                continue
            guards.add(pos)

            ans += is_loop(start, guards, dim)

            guards.remove(pos)
    return ans



def main():
    assert solve1(EXAMPLE) == 41
    assert solve2((EXAMPLE)) == 6

    with open('day6.txt') as f:
        my_input = f.read()

    print(solve1(my_input))
    print(solve2(my_input))

main()
