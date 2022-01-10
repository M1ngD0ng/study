C=int(input())
A=[]
for i in range(C):
  X=list(map(int,input().split()))
  A.append(X)

for j in range(C):
  cnt=0
  N=(sum(A[j])-A[j][0])/A[j][0]
  for k in range(1,len(A[j])):
    if A[j][k]>N:
      cnt+=1
  s='{:.3f}%'.format((cnt/A[j][0])*100)
  print(s)