import functools


EXAMPLE="125 17"


@functools.lru_cache(None)
def rec(a: int, n: int) -> int:
    if n == 0:
        return 1

    if a == 0:
        return rec(1, n-1)
    s = str(a)
    l = len(s)
    if l%2==0:
        return rec(int(s[:l//2]),n-1) + rec(int(s[l//2:]),n-1)
    else:
        return rec(a*2024, n-1)


def solve(s: str, n: int) -> int:
    ans = 0
    for a in map(int, s.strip().split()):
        ans += rec(a, n)
    return ans


def main():
    print(solve(EXAMPLE, n=25))
    print(solve(EXAMPLE, n=75))

    with open('day11.txt') as f:
        my_input = f.read()
        print(solve(my_input, n=25))
        print(solve(my_input, n=75))


main()
