N=int(input())

cntAll=[0,0,1,1] # 3까지 값을 초기화

for i in range(4,N+1):
  if (cntAll[i//3]+i%3)<(cntAll[i//2]+i%2):
    cntAll.append(cntAll[i//3]+i%3+1)
  else:
    cntAll.append(cntAll[i//2]+i%2
    +1)

print(cntAll[N])
