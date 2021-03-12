import cmath

"""
x=input()
r,phi=abs(complex(x)),cmath.phase(complex(x))
"""
r,phi=cmath.polar(complex(input()))

print(r,phi,sep='\n')