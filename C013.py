n=int(input())

i=0
while i<n:
    ma=int(input())
    me=ma
    soma=ma
    i=i+1
    while i<n:
        x=int(input())
        if x>ma:
            ma=x
        if x<me:
            me=x
        i=i+1
        soma=soma+x

print(ma)
print(me)
print(soma)