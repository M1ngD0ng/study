import sys
N,X=map(int,input().split())
A=list(map(int, input().split()))
for i in range(N):
  if A[i]<X:
    sys.stdout.write(str(A[i])+' ')
