# 問題文
# N個の整数A1,A2,...,ANの中に、整数Xが含まれるか
# どうかを判定するプログラムを作成する

# 05.20
N,X = map(int,input().split())
A   = list(map(int,input().split()))
Ans = False

for i in range(N):
    if X==A[i]:
        Ans = True

if Ans==True:
    print("Yes")
else:
    print("No")