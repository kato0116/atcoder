H,W = map(int,input().split())

X = [None]*(H+1)
X[0] = [0]*(W+1)

for i in range(H):
    w = list(map(int,input().split()))
    tmp = [None]*(W+1)
    tmp[0] = 0
    for j in range(W):
        tmp[j+1] = tmp[j]+w[j]   
    X[i+1] = tmp

for i in range(1,H+1):
    for j in range(W+1):
        X[i][j] = X[i-1][j]+X[i][j]
        
Q = int(input())

A = [None]*Q
for j in range(Q):
    A[j] = list(map(int,input().split()))
for i in range(Q):
    ANS = X[A[i][2]][A[i][3]]-X[A[i][0]-1][A[i][3]]-X[A[i][2]][A[i][1]-1]+X[A[i][0]-1][A[i][1]-1]
    print(ANS)