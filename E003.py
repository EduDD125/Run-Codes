str = input()
char = input()
a=0

i=0
while i<len(str):
    if char == str[i]:
        a=a+1
    i=i+1

print(a)