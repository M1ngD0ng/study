A=1
B=1
C=[]
while True:
  A, B= map(int, input().split())
  if A==0 and B==0:
    break
  C.append(A+B)

for i in range(len(C)):
  print(C[i])