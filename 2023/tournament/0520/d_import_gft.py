import sys
input = sys.stdin.readline
N, M, D = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 制約条件
# a-b <= D
A.sort(set(A))
B.sort(set(B))

print(A)
print(B)