t=[]

i=0
soma=0
while i<7:
    x=float(input("digite temperatura:   "))
    t.append(x)
    soma=soma+x
    i=i+1

i=0
a=0
while i<7:
    if t[i]>soma/7:
        a=a+1
    i=i+1

print(a)