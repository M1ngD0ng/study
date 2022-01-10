import sys
N=input()

A=[]
for i in str(N):
  A.append(i)
A.sort(reverse=True)

for j in range(len(A)):
  sys.stdout.write(A[j])
