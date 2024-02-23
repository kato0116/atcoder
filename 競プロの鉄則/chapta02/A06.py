# 2023.7.3
# TLEが発生。解答見た。ポイントは、2日目まで、3日目まで...ｎ日までの入場者数を先に計算するがポイント

import sys

N, Q = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
L = [None]*Q
R = [None]*Q

for i in range(Q):
    L[i],R[i] = map(int,input().split())
S    = [None]*(N+1)
S[0] = 0
for j in range(N):
    S[j+1] = S[j]+A[j]
for i in range(Q):
    print(S[R[i]]-S[L[i]-1])