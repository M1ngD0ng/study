data=list(input().split())
A=[]
B=[]

for s in str(data[0]):
  A.append(s)
for t in str(data[1]):
  B.append(t)
 
rev_A=''.join(A[::-1])
rev_B=''.join(B[::-1])
if int(rev_A)>int(rev_B):
  print(rev_A)
else:
  print(rev_B)
