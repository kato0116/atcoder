A,B = map(int,input().split())

flag = False
for i in range(3):
    if ((3*i+1)<=A and A<=3*(i+1)) and ((3*i+1)<=B and B<=3*(i+1)) and abs(A-B)==1:
        flag = True
if flag:
    print("Yes")
else:
    print("No")