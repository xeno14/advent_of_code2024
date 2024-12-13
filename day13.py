import re
import itertools


EXAMPLE="""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


def sol(ax, ay, bx, by, px, py):
    det = ax*by - ay*bx
    if det == 0:
        return None

    alpha = px*by - bx*py 
    if alpha % det != 0:
        return None

    beta = ax*py - px*ay
    if beta % det != 0:
        return None

    return alpha//det, beta//det



def parse(s: str):
    for part in s.strip().split('\n\n'):
        a, b, p = re.findall(r'X.([0-9]+), Y.([0-9]+)', part)
        yield tuple(map(int, itertools.chain(a, b, p)))


def solve1(s:str):
    ans = 0
    for ax,ay,bx,by,px,py in parse(s):
        xy = sol(ax, ay,bx,by,px,py)
        if xy is None:
            continue
        x, y = xy

        ans += 3*x + y
    return ans

OFFSET = 10000000000000
def solve2(s:str):
    ans = 0
    for ax,ay,bx,by,px,py in parse(s):
        xy = sol(ax, ay,bx,by,px+OFFSET,py+OFFSET)
        if xy is None:
            continue
        x, y = xy

        ans += 3*x + y
    return ans


def main():
    assert solve1(EXAMPLE) == 480

    with open('day13.txt') as f:
        my_input = f.read()
        print(solve1(my_input))
        print(solve2(my_input))


main()
