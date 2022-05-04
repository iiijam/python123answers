n,k=map(int,input().split())

if k<2 or n<k:
    print('Data Error!')

else:
    answer=[i for i in range(1,n+1)]

    while len(answer)>=k:
        answer=answer[k:]+answer[:k-1]

    print(answer)