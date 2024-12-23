import collections
import itertools

EXAMPLE="""
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

def parse(s:str):
    import re
    g = collections.defaultdict(set)
    for x, y in re.findall(r'(.+)-(.+)', s.strip()):
        g[x].add(y)
        g[y].add(x)
    return g


def find_three_connected(g):
    for a, b, c in itertools.combinations(g.keys(), r=3):
        if a in g[b] and b in g[c] and c in g[a]:
            yield a, b, c


def solve1(s:str):
    g = parse(s)

    ans = 0
    for a, b, c in find_three_connected(g):
        ans += any(x.startswith('t') for x in [a, b, c])
    return ans


def find_all_connected(g, a, b, c):
    q = collections.deque(g[a] | g[b] | g[c])
    connected = set([a, b, c])

    while q:
        u = q.popleft()
        if u in connected:
            continue
        if all(u in g[v] for v in connected):
            connected.add(u)
            q.extend([v for v in g[u] if v not in connected])
    return connected


def solve2(s):
    g = parse(s)

    connected_list = []
    for a, b, c in find_three_connected(g):
        connected = find_all_connected(g, a, b, c)
        connected_list.append(connected)
    
    connected_list.sort(key=lambda x: -len(x))
    print(connected_list[:3])
    return ','.join(sorted(connected_list[0]))


def main():
    print(solve1(EXAMPLE))
    print(solve2(EXAMPLE))

    with open('day23.txt') as f:
        my_input = f.read()

    print(solve1(my_input))
    print(solve2(my_input))



main()
