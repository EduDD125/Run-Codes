# ENTRADA:
a = int(input())
b = int(input())
c = int(input())

# PROCESSAMENTO:
d = a
e = b
f = c

#d>e>f
if d>=e and e>=f:
    a=f
    b=e
    c=d
#d>f>e
elif d>=f and f>=e:
    a=e
    b=f
    c=d
######
#e>d>f
elif e>=d and d>=f:
    a=f
    b=d
    c=e
#e>f>d
elif e>=f and f>=d:
    a=d
    b=f
    c=e
######
#f>d>e
elif f>=d and d>=e:
    a=e
    b=d
    c=f
#f>e>d
elif f>=e and e>=d:
    a=d
    b=e
    c=f

# SAIDA:
print(a)
print(b)
print(c)