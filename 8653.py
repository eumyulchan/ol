import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c = list(map(int, input().split()))
cb = max(c)
cbe = c.index(cb)
def solve(d):
    s = 0
    e = a
    ans = 0
    wns = 0
    while True:
            mid = (s+e)//2   
            if mid == cbe and d == c[mid]:
                print("T")
                break
            elif d == c[mid] and mid < cbe:
                print("L")
                break
            elif d == c[mid] and mid > cbe:
                print("R")
                break

            else:
                e = mid -1
                
                if s == e:
                   ans +=1
           
                if ans >= 2:
                    s = (s+a)//2
                    
                    e = a
                    wns +=1
                if wns >= 2:
                    print("N")
                    break   
                elif s > e:
                    print("N")
                    break
           
for i in range(b):
    se = int(input())
    solve(se)
    se = 0