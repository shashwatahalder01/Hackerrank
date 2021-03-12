if __name__ == '__main__':
    l=[]
    s=[]
    n=[]
    for _ in range(int(input())):
            name = input()
            score = float(input())
            l.append([name,score])
            s.append(score)
    s=list(set(s))
    s.sort()
    """
    for x in range(len(l)):
        if l[x][1] == s[-2]:
            n.append(l[x][0])
            """
    n=[l[x][0] for x in range(len(l)) if l[x][1] == s[1]]
    n.sort()
    print('\n'.join(map(str, n)))
