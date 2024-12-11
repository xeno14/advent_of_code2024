import collections


def parse(s: str):
    for line in s.strip().split('\n'):
        left, right = line.split(':')
        n = int(left)
        values = list(map(int, right.strip().split()))
        yield n, values


def evaluate(n, values):
    q = collections.deque([values[0]])

    for x in values[1:]:
        l = len(q)
        for _ in range(l):
            l = q.popleft()
            q.append(x + l)
            q.append(x * l)

    return n in q


def solve1(s: str):
    return sum(n for n, values in parse(s) if evaluate(n, values))


def evaluate2(n, values):
    q = collections.deque([values[0]])

    for r in values[1:]:
        l = len(q)
        for _ in range(l):
            y = q.popleft()
            q.append(r + y)
            q.append(r * y)
            q.append(int(str(y)+ str(r)))

    # print(n, values, q)
    return n in q

def solve2(s: str):
    return sum(n for n, values in parse(s) if evaluate2(n, values))


EXAMPLE = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
        

def main():
    print(solve1(EXAMPLE))
    print(solve2(EXAMPLE))

    with open('day7.txt') as f:
        my_input = f.read()

    print(solve1(my_input))
    print(solve2(my_input))

main()
