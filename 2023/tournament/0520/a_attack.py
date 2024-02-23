# 05.20

A, B = map(int,input().split())

tmp = A//B
if (A%B)==0:
    print(tmp)
else:
    print(tmp+1)
