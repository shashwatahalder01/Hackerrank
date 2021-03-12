if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = divmod(a, b)
    a,b=c
    print(a,b,c, sep="\n")
      