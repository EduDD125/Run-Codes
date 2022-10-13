str = input()


if len(str)>1:
    i=-1
    while i>-len(str):
        print(str[i],end=" ")
        i=i-1
    print(str[i])
else:
    print(str[0])