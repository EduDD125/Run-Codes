str = input()
i=0
if len(str)>1:
    while i<len(str)-1:
        print(str[i],end=" ")
        i=i+1
    print(str[i])
else:
    print(str[i])