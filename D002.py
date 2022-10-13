n = int(input())
l=[]
str=""

i=0
while i<n:
    x = input()
    l.append(x)
    i=i+1

i=0
while i<n:
    if  i==0:
        str = str + l[i]
    else:
        str = str + " " + l[i]
    i=i+1

print(str)