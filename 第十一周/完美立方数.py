N=int(input())
for i in range (2,N+1):
    a=i
    for i in range (2,N+1):
        b=i
        for i in range (b,N+1):
            c=i
            for i in range (c,N+1):
                d=i
                if pow(a,3)==pow(b,3)+pow(c,3)+pow(d,3):
                    print("Cube = {:.0f},Triple = ({:.0f},{:.0f},{:.0f})".format(a,b,c,d))