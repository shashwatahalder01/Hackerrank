cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    l=[0,1]
    i=2
    while i < n:
        l.append(l[i-1]+l[i-2])
        i+=1
        #print(l)
    return l[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))