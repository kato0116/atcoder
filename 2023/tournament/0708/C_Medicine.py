N, K = map(int, input().split())
ab = [None]*N

sum_b = 0
for i in range(N):
    ab[i] = list(map(int,input().split()))
    sum_b += ab[i][1]
ab = sorted(ab)
day = 0
i   = 0
while True:
    if sum_b <= K:
        day += 1
        break
    day = ab[i][0] #日数を更新
    sum_b -= ab[i][1] # 錠数を減算
    i += 1
print(day)