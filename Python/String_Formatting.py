
def print_formatted(number):
    l=len(bin(number).replace("0b",""))

    for x in range(1,n+1):
        de=str(x)
        oc=oct(x).replace("0o", "")
        he=str(hex(x).replace("0x", "")).upper()
        bi=str(bin(x).replace("0b", ""))
        print(de.rjust(l),oc.rjust(l),he.rjust(l),bi.rjust(l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
 
"""
def print_formatted(number):
    l=len(bin(number).replace("0b",""))

    for x in range(1,n+1):
        de=str(x)
        oc=oct(x).replace("0o", "")
        he=str(hex(x).replace("0x", "")).upper()
        bi=str(bin(x).replace("0b", ""))
        dd=l-len(de)
        od=l-len(oc)
        hd=l-len(he)
        bd=l-len(bi)
        print(' '*dd+de+' '+' '*od+oc+' '+' '*hd+he+' '+' '*bd+bi)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    """