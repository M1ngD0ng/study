from collections import Counter

data=input()
A=[]
for s in str(data):
  A.append(s.lower())
cnt=Counter(A)
if len(A)>1:
  most=cnt.most_common(2)
  if most[0][1]==most[1][1]:
    print('?')
  else:
    print(most[0][0].upper())
else:
  print(A[0].upper())