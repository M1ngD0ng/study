import sys
N=int(sys.stdin.readline().rstrip())
A=[]
for _ in range(N):
  B=int(sys.stdin.readline().rstrip())
  A.append(B)

A.sort()
for i in range(0,N):
  print(A[i])