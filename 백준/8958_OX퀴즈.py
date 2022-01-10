N=int(input())
A=[]
cntTotal=0
cnt=0
for _ in range(N):
  A.append(input())

for i in range(len(A)):
  cntTotal=0
  cnt=0
  for j in range(0,len(A[i])):
    if A[i][j]=='O':
      cnt+=1
    elif A[i][j]=='X':
      cnt=0
    cntTotal=cntTotal+cnt
  print(cntTotal)