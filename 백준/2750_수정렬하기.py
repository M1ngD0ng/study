N=int(input())
A=[]
for _ in range(N):
  B=int(input())
  A.append(B)

A.sort()
for i in range(N):
  print(A[i])