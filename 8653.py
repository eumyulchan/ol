import sys
input = sys.stdin.readline
n,q = map(int, input().split())
l = list(map(int, input().split()))
ql = list(map(int, input().split()))
o = 0
c = []
c = set(l)

def solve(ab):
    s = 0
    e = n-1
    ol = 0
   
    while True:

        mid = (s+e)//2
        
        if l[mid] == ab:
        
            break
        elif l[mid] > ab:
            e = mid - 1
         
        elif l[mid] < ab:
            s = mid+1
        if s>e:
            ol += 1
            print(ab, end = ' ')
            
            return ol
           

for i in ql:
    solve(i)
ol = ol + solve(i)

if  ol == 0:
    print(-1)
