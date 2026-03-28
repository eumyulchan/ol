l=[]
e = 0
for i in range(100):
    l.append([0]*100)
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    for dd in range(b,b+10):
         for i in range(a,a+10):
             l[i][dd] = 1
for i in range(100):
    for dd in range(100):
        if l[i][dd] == 1:
            e +=1
print(e)



