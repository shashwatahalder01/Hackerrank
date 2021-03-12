l=[]
m,n=(map(int, input().split()))
for x in range(0,n):
    l.append(list(map(float, input().split())))
z=list(zip(*l))
for x in z:
    print(format(sum(x)/n, '.1f'))
