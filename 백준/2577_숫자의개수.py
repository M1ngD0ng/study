A=int(input())
B=int(input())
C=int(input())

res=A*B*C
char=[]
for i in str(res):
  char.append(int(i))

cnt=[]
for j in range(0,10):
  cnt.append(char.count(j))
for k in range(0,10):
  print(cnt[k])