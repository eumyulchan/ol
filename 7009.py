import sys
input = sys.stdin.readline
n,q = map(int, input().split())
l = list(map(int, input().split()))
ql = list(map(int, input().split()))
o = 0
c = []
l.sort()
ans = 0
ans1 = 0
def solve(ab):
    s = 0
    e = n-1
   
   
    while True:

        mid = (s+e)//2
        
        if l[mid] == ab:
            
            return 1
        elif l[mid] > ab:
            e = mid - 1
        elif l[mid] < ab:
            s = mid+1
        if s>e:
            return 0
           

for i in ql:
    solve(i)
    ans = solve(i)
    ans1 = ans1 + ans
    if ans == 0:
        print(i, end = ' ')
if  ans1 == q:
    print(-1)
