N, K = map(int,input().split())

ans = 0
for x in range(1,N+1):
    for y in range(1,N+1):
        z = K-x-y
        if z>=1 and z <=N:
            ans += 1

print(ans)