import numpy as np
N = int(input())
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]
for i in range(N):
    A[i],B[i] = map(int,input().split())

clear_p = [0 for _ in range(N)]
for i in range(N):
    clear_p[i] = A[i]/(A[i]+B[i])
ranking_p = np.sort(clear_p)[::-1]
ranking  = np.argsort(clear_p)[::-1]
ranking_p = ranking_p.tolist()
for i in range(1,N):
    M = ranking_p.count(ranking_p[i])
    if M>1:
        print(sorted(ranking[i+M+1:]))
        tmp = ranking[:i-1] + sorted(ranking[i-1:i+M+1])+ranking[i+M+1:]
        print(tmp)
        
print(len(ranking))     
for i in range(N):
    ranking[i] += 1

print(ranking)