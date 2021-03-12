if __name__ == '__main__':
    l=[]
    res=[]
    N = int(input())
    for _ in range(N):
        l.append(input().split())

    for x in l:
        if "insert" in x:
            res.insert(int(x[1]),int(x[2]))
        elif "print" in x:
            print(res)
        elif "remove" in x:
            res.remove(int(x[1]))
        elif "append" in x:
            res.append(int(x[1]))
        elif "sort" in x:
            res.sort()
        elif "pop" in x:
            res.pop()
        elif "reverse" in x:
            res.reverse()
        
    """    
    l=[]
    res=[]
    N = int(input())
    for _ in range(N):
        x=input().split()
        if "insert" in x:
            res.insert(int(x[1]),int(x[2]))
        elif "print" in x:
            print(res)
        elif "remove" in x:
            res.remove(int(x[1]))
        elif "append" in x:
            res.append(int(x[1]))
        elif "sort" in x:
            res.sort()
        elif "pop" in x:
            res.pop()
        elif "reverse" in x:
            res.reverse()
           """ 
            
