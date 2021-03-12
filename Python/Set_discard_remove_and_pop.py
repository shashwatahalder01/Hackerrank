
n = int(input())
s = set(map(int, input().split()))

l=[]
N = int(input())
for _ in range(N):
    l.append(input().split())

for x in l:
    if "discard" in x:
        s.discard(int(x[1]))
    elif "remove" in x:
        s.remove(int(x[1]))
    elif "pop" in x:
        s.pop()

print(sum(s))