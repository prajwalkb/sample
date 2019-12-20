T=int(input())
c=0
for _ in range(T):
    s=int(input())
    for i in range(0,s*3,3):
        if s<i:
            c+=1
            break
    print(c)



