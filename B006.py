a=float(input())
b=float(input())
c=float(input())

delta=(b**2)-(4*a*c)

if delta>=0:
    x1=(-b+(delta**(1/2)))/(2*a)
    x2=(-b-(delta**(1/2)))/(2*a)
    soma=x1+x2
    print(f"{soma:.2f}")
else:
    import math
    print(math.nan)
    