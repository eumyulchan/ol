import sys
input = sys.stdin.readline
a = int(input())
l = list(map(int, input().split()))
b = int(input())
l1 = list(map(int, input().split()))

def solve(ab):
    s = 0
    e = a-1
   
   
    while True:

        mid = (s+e)//2
        
        if l[mid] == ab:
        
            print(mid, end = ' ')
            break
        elif l[mid] > ab:
            e = mid - 1
        elif l[mid] < ab:
            s = mid+1
        if s>e:
            print(-1, end = ' ')
            break

for i in l1:
    solve(i)