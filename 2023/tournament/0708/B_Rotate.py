N = int(input())

A  = [None]*N
A2 = [None]*N
for i in range(N):
    A[i]= (input())
    A2[i] = A[i]
print(A[0])
A[0][2]=2
print(A[0])