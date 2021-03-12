
n,m=map(int,input().split())
a=1
b=(m-3)//2
for x in range(1,int((n+1)/2)):
    print('-'*b+'.|.'*a+'-'*b)
    a+=2
    b-=3
print('-'*int((m-7)//2)+'WELCOME'+'-'*int((m-7)//2))
for x in range(1,int((n+1)/2)):
    a-=2
    b+=3
    print('-'*b+'.|.'*a+'-'*b)
