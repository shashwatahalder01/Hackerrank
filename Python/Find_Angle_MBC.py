import math
if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    mbc=round(math.degrees(math.atan(ab/bc)))
    """
        alternative of round
    g=math.ceil(mbc)
    l=math.floor(mbc)
    if (g-mbc)>(mbc-l):
        mbc=g
    else:
        mbc=l
    """
    print(mbc,"°", sep='') 