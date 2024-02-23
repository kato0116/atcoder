def reversal(A,L,R):
    tmp = []
    for i in range(L):
        tmp.append(A[i])

    for j in range(R-L+1):
        tmp.append(A[R-j])

    for k in range(R+1,len(A)):
        tmp.append(A[k])   
     
    return tmp


        

NK = list(map(int,input().split()))
A  = list(map(int,input().split()))
N = NK[0]
K = NK[1]
A_list = []
for L in range(N):
    for R in range(L,N):
        A_list.append(reversal(A,L,R))
A_list.sort()
print(*A_list[K-1])
