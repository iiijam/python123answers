from random import randint, seed

seed(int(input()))

p = int(input())

A = []
B = []

for i in range(1, 6):
    A.append([i, randint(0, 100), randint(0, 100)])
    B.append([i, randint(0, 100)])

for c in B:
    for i in range(5):
        if c[0] == A[i][0]:
            A[i].insert(p, c[1])

print(A)
