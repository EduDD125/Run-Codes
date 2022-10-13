l=int(input())
m=float(input())
a=float(input())
v=int(input())

multa=m+a*(v-l)

if v>l:
    multa=m+a*(v-l)
    print(f"{multa:.2f}")
else:
    multa=0
    print(f"{multa:.2f}")