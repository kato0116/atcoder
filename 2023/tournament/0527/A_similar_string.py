N = int(input())
S = str(input())
T = str(input())
check = True
for i in range(N):
    if S[i]==T[i] or S[i]:
        continue
    elif ((S[i]== "1")or(S[i]== "l"))and((T[i]=="1")or(T[i]=="l")):
        continue
    elif ((S[i]== "0")or(S[i]== "o"))and((T[i]=="0")or(T[i]=="o")):
        continue
    else:
        check=False
        break
if check==True:
    print("Yes")
else:
    print("No")
