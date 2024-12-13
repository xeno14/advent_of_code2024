import collections


EXAMPLE = """
..X...
.SAMX.
.A..A.
XMAS.S
.X....
"""

EXAMPLE2="""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def parse(s: str):
    res = collections.defaultdict(set)
    for y, line in enumerate(s.strip().split('\n')):
        for x in range(len(line)):
            c = line[x]
            if c in 'XMAS':
                res[c].add((x, y))
    return res



def is_word(data, pos, word):
    x, y = pos

    res = 0
    for locations in (
        # horizontal
        [(x+i, y) for i in range(len(word))],
        [(x-i, y) for i in range(len(word))],
        # vertical
        [(x, y+i) for i in range(len(word))],
        [(x, y-i) for i in range(len(word))],
        # diagonal
        [(x+i, y+i) for i in range(len(word))],
        [(x+i, y-i) for i in range(len(word))],
        [(x-i, y+i) for i in range(len(word))],
        [(x-i, y-i) for i in range(len(word))],
    ):
        if all(locations[i] in data[word[i]] for i in range(len(word))):
            res += 1
    return res


def visualize(space, dim):
    data = [
        ['.'] * dim[0] for _ in range(dim[1]) 
    ]

    for pos in space:
        x, y = pos
        data[y][x] = 'X'

    for l in data:
        print(''.join(l))



def solve1(s:str):
    data = parse(s)

    ans = 0
    word = 'XMAS'
    locs = []
    for pos in data[word[0]]:
        a = is_word(data, pos, word)
        if a:
            locs.append(pos)
        ans += a
    # visualize(locs, (10, 10))
    return ans


def is_xmas(data, pos):
    if pos not in data['A']:
        return False

    x, y = pos

    lu = (x-1, y-1)
    ru = (x+1, y-1)
    ld = (x-1, y+1)
    rd = (x+1, y+1)

    cnt = 0
    cnt += lu in data['M'] and rd in data['S']
    cnt += rd in data['M'] and lu in data['S']
    cnt += ld in data['M'] and ru in data['S']
    cnt += ru in data['M'] and ld in data['S']

    return cnt == 2


def solve2(s:str):
    data = parse(s)

    ans = 0
    for pos in data['A']:
        ans += is_xmas(data, pos)
    return ans


def main():
    assert solve1(EXAMPLE) == 4
    assert solve1(EXAMPLE2) == 18
    print(solve2(EXAMPLE2))

    with open('day4.txt') as f:
        my_input = f.read()

    print(solve1(my_input))
    print(solve2(my_input))

main()
