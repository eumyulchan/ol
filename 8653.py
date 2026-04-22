import sys
input = sys.stdin.readline
ced, b = map(int, input().split())
c = list(map(int, input().split()))

cb = max(c)
cbe = c.index(cb)
def solve(d):
    s = 0
    e = ced
    while True:
         mid = (s+e)//2
            
         if mid == cbe:
             print("T")
             break
         elif d == c[mid] and mid > cbe:
            print("L")
            break
         elif d == c[mid] and mid < cbe:
             print("R")
             break

         elif c[mid] > c.index(d):
               e = mid - 1
         elif c[mid] < c.index(d):
               s = mid + 1
         if s > e:
             print("N")
             break
            
for i in range(b):
    se = int(input())
    solve(se)
    se = 0