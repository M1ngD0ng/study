import math

A,B,C=map(int,input().split())


if B>=C:
  print(-1)
else:
  N=math.ceil(A/(C-B))
  if (A/(C-B))==N:
    N+=1
    print(N)
  else:
    print(N)