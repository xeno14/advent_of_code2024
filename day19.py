import functools


EXAMPLE="""
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

EXAMPLE2="""
r, wr, b, g, bwu, rb, gb, br

gbbr
rrbgbr
"""



def parse(s:str):
    parts = s.strip().split('\n\n')

    towels = parts[0].split(', ')
    designs = parts[1].split('\n')
    return towels, designs


def solve1(s:str):
    towels, designs = parse(s)

    @functools.cache   
    def rec(d:str) -> bool:
        for t in towels:
            if t == d:
                return True
            if d.startswith(t) and rec(d[len(t):]):
                return True
        return False

    ans = 0
    for design in designs:
        p = rec(design)
        print(design, p)
        ans += p
    return ans


def solve2(s:str):
    towels, designs = parse(s)
    towels.sort()

    @functools.cache   
    def rec(d:str) -> bool:
        if len(d) == 0:
            return 1
        cnt = 0
        for t in towels:
            if d.startswith(t):
                cnt += rec(d[len(t):])
        return cnt

    ans = 0
    for design in designs:
        p = rec(design)
        print(design, p)
        ans += p
    return ans


def main():
    print(solve1(EXAMPLE))
    print(solve2(EXAMPLE2))

    with open('day19.txt') as f:
        my_input = f.read()

    print(solve1(my_input))
    print(solve2(my_input))



main()

