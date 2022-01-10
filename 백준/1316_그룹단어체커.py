N=int(input())
A=[]

for _ in range(N):
  A.append(input())

cnt=0
for s in A:
  check=True
  test=[]
  test.append(s[0])
  for i in range(1,len(s)):
    if s[i-1]!=s[i]:
      if s[i] not in test:
        test.append(s[i])
      elif s[i] in test:
        check=False
        break
  if check==True:
    cnt+=1

print(cnt)