import sys
sys.setrecursionlimit(10000)

carte = []
with open('input.txt','r') as f:
    for ligne in f.read().splitlines():
        carte.append(ligne)

n, m = len(carte), len(carte[0])

def voisins( pos ):
    i, j = pos
    if carte[i][j] == '>': return [(i,j+1)]
    if carte[i][j] == '<': return [(i, j-1)]
    if carte[i][j] == '^': return [(i-1,j)]
    if carte[i][j] == 'v': return [(i+1, j)]

    voisinspot = [(i-1,j), (i+1,j), (i,j-1), (i,j+1) ]
    if carte[i][j] == '.':
        return [(i,j) for (i,j) in voisinspot if i >= 0 and j >= 0 and i < n and j < m and carte[i][j] != '#']

def DFS(start, end, init_dist, vus):
    if start == end:
        yield init_dist

    for v in voisins(start):
        if v not in vus:
            vus.add(v)
            yield from DFS(v, end, init_dist + 1, vus)
            vus.remove(v)

deb = (0,1)
fin = (n-1, m-2)

print('Part 1 :',max(DFS(deb,fin,0,{deb})))

## Part 2
from time import time
def voisins2( pos ):
    i, j = pos
    voisinspot = [(i-1,j), (i+1,j), (i,j-1), (i,j+1) ]
    return [(i,j) for (i,j) in voisinspot if i >= 0 and j >= 0 and i < n and j < m and carte[i][j] != '#']


# Contracted graph
bifurcations = [deb] + [(i,j) for i in range(n) for j in range(m) if len(voisins2((i,j))) > 2  ] + [fin]
#G = {bif: [ ] for bif in bifurcations}
from collections import defaultdict
G = defaultdict(list)
for b in bifurcations:
    for v in voisins2(b):
        previous, cur = b, v
        d = 1
        while cur not in bifurcations:
            previous, cur = cur, [p for p in voisins2(cur) if p != previous][0]
            d += 1
        G[b].append((cur, d))


def DFS2(start, end, init_dist, vus):
    if start == end:
        yield init_dist

    for v, d in G[start]:
        if v not in vus:
            vus.add(v)
            yield from DFS2(v, end, init_dist + d, vus)
            vus.remove(v)

print('Part 2 :',max(DFS2(deb,fin,0,{deb})))