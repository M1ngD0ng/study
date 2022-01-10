A=[]
B=[]
for i in range(10):
  A.append(int(input()))
  B.append(A[i]%42)
cnt=0
sett=set(B)
print(len(sett))