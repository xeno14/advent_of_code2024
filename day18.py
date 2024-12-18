import collections

EXAMPLE="""
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""


def parse(s: str):
    for line in s.strip().split('\n'):
        yield tuple(map(int, line.split(',')))


def bfs(walls, xmax, ymax, first_n_bytes):
    walls = walls[:first_n_bytes]

    start = (0, 0)
    goal = (xmax, ymax)

    dist = {}
    for wall in walls:
        dist[wall] = -1

    q = collections.deque([(start, 0)])
    while q:
        pos, d = q.popleft()
        if not (0 <= pos[0] <= xmax and 0 <= pos[1] <= ymax) or pos in dist:
            continue
        dist[pos] = d

        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx = pos[0] + dx
            ny = pos[1] + dy
            q.append(((nx, ny), d+1))
    return dist.get(goal)


def solve1(s: str, xmax, ymax, first_n_bytes):
    return bfs(list(parse(s)), xmax, ymax, first_n_bytes)


def solve2(s, xmax, ymax):
    walls = list(parse(s))

    def has_path(n):
        return bfs(walls, xmax, ymax, n) is not None

    left = 1
    right = len(walls)
    while right - left > 1:
        mid = (right + left) // 2
        if has_path(mid):
            left = mid
        else:
            right = mid
    return '%d,%d'%(walls[right-1])



def main():
    print(solve1(EXAMPLE, xmax=6, ymax=6, first_n_bytes=12))
    print(solve2(EXAMPLE, xmax=6, ymax=6))

    with open('day18.txt') as f:
        my_input = f.read()
        print(solve1(my_input, xmax=70, ymax=70, first_n_bytes=1024))
        print(solve2(my_input, xmax=70, ymax=70))

main()
