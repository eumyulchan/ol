import sys
input = sys.stdin.readline
n,q = map(int, input().split())
l = list(map(int, input().split()))
c = max(l)
acb = c
c = l.index(c)
b =[]
d = []
sum = 0
sum1 = 0
for i in range(0, c):
    b.append(l[i])
   
    sum+=1
for i in range(c+1, n):
    d.append(l[i])
    sum1+=1
bb = max(b)
d.sort()
di = max(d)

def solve(ab):
    if acb == ab:
        return 'T'
    else:
        return 'N'
def solve1(ab):
    s = 0
    e = sum-1
    while True:
        mid = (s+e)//2
        if b[mid] == ab:
            return 'L'
        elif b[mid] > ab:
            e = mid - 1
        elif b[mid] < ab:
            s = mid+1
        if s>e:
            return 'N'
def solve2(ab):
    s = 0
    e = sum1-1
    while True:
        mid = (s+e)//2
        if d[mid] == ab:
            return 'R'
        elif d[mid] > ab:
            e = mid - 1
        elif d[mid] < ab:   
            s = mid+1
        if s>e:
            return 'N'
for i in range(q):
    a = int(input())
    solve(a)
    solve1(a)
    solve2(a)
    if solve(a) == 'T':
        print("T")
    elif solve1(a) == 'L':
        print("L")
    elif solve2(a) == 'R':
        print("R")
    if solve(a) == 'N' and solve1(a) == 'N' and solve2(a) == 'N':
        print("N")