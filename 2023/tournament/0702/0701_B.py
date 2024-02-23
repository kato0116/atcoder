N,M = map(int,input().split())
C = list(map(str,input().split()))
D = list(map(str,input().split()))
P = list(map(int,input().split()))

# Cが食べたお皿の色
# Dがお皿の色の種類、PがDの色に対応する値段
# お皿の枚数をカウントする
count_dish = [0 for _ in range(len(D))]
c_count = 0
sum_money = 0
sum_count = 0

for i in range(len(D)):
    count = C.count(D[i])
    sum_count += count
    sum_money += count*P[i+1]
sum_money += (len(C)-sum_count)*P[0]
print(sum_money)