n,m=map(int,input().split())
for i in range(0,1,100):
    if n>=5 and m>10:
        print(n+(m//n))
        break
    else:
        print(n-(m//n))
        break