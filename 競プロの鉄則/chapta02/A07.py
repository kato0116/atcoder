# 2023.07.3
# どうしても二重ループを消す方法が思い浮かばなかった...
# 前日比用意したら、0日目を0として始めると前日比を加算していくだけの計算に持っていける
# くやしめ

D = int(input())
N = int(input())
L = [None]*N
R = [None]*N
for i in range(N):
    L[i],R[i] = map(int,input().split())

# 前日比のリストを用意
B = [0]*(D+2)

for i in range(N):
    B[L[i]] += 1
    B[R[i]+1] -= 1 # R日目まで参加している。そのためR+1日目は参加しない。そのため前日比は-1
    
S = [0]*(D+1)
for j in range(1,D+1):
    S[j] = S[j-1]+B[j]
    print(S[j])