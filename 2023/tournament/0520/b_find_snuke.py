# 05.20
H, W = map(int,input().split())
S = []
for i in range(H):
    s = str(input())
    S.append(s)
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for i in range(H):
    for j in range(W):
        for k in range(8): # 8方向探索
            tmp = ""
            for t in range(5): # 文字数の連続性を見る
                y,x = i+t*dy[k], j+t*dx[k]
                if  H<=y or y<0 or W<=x or x<0:
                    break
                tmp += S[y][x]
            if tmp == "snuke":
                for p in range(5):
                    y,x = i+p*dy[k]+1, j+p*dx[k]+1
                    print(y,x)
                exit()




