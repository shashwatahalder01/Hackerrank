def swap_case(s):
    return s.swapcase()
"""
def swap_case(s):
    a=""
    for x in s:
     if x.islower():
          a+=x.upper()
     else:   
          a+=x.lower()
    return a
"""
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)