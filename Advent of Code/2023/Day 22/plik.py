import sys
sys.setrecursionlimit(1000000)
ans = res = 0

with open("input.txt") as f:
    s = f.read().strip()


bricks = []
# line by line input
for l in s.split("\n"):
    sloc,eloc = l.split("~")
    sx,sy,sz = map(int,sloc.split(","))
    ex,ey,ez = map(int,eloc.split(","))
##    sx,ex = min(sx,ex),max(sx,ex)
##    sy,ey = min(sy,ey),max(sy,ey)
##    sz,ez = min(sz,ez),max(sz,ez)
    bricks.append((sx,sy,sz,ex,ey,ez))

# z is vertical direction
# z = 0

def is_solid(bset, x,y,z):
    if z == 0:
        return True
    return (x,y,z) in bset
##    for (sx,sy,sz,ex,ey,ez) in bricks:
##        if x in range(sx,ex+1) and y in range(sy,ey+1) and z in range(sz,ez+1):
##            return True
    ##return False

def bfall(bricks):
    fell = False
    bset = set()
    for (sx,sy,sz,ex,ey,ez) in bricks:
        for x in range(sx,ex+1):
            for y in range(sy,ey+1):
                bset.add((x,y,ez))
    
    new_bricks = []
    for b in bricks:
        supp = False
        sx,sy,sz,ex,ey,ez = b
        for x in range(sx,ex+1):
            for y in range(sy,ey+1):
                # is (x,y,sz-1) solid?
                if is_solid(bset, x, y, sz - 1):
                    supp = True
                    break
            if supp:
                break
        if not supp:
            fell = True
            new_bricks.append((sx,sy,sz-1, ex,ey,ez-1))
        else:
            new_bricks.append(b)
    return fell, new_bricks


fell = True
cnt = 0
while fell:
    cnt += 1
    fell, bricks = bfall(bricks)

bcopy = bricks.copy()

ans = 0
for i in range(len(bcopy)):
    bcopy2 = bcopy.copy()
    del bcopy2[i]
    if not bfall(bcopy2)[0]:
        ans += 1
print(ans)

ans = 0
for i in range(len(bcopy)):
    bcopy2 = bcopy.copy()
    del bcopy2[i]
    bcopy3 = bcopy2.copy()
    fell = True
    while fell:
        fell, bcopy2 = bfall(bcopy2)
    mm = 0
    for a,b in zip(bcopy2, bcopy3):
        if a != b:
            mm += 1
    ans += mm
print(ans)