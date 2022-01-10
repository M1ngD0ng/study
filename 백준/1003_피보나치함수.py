T=int(input())
case=[]

for _ in range(T):
  case.append(int(input()))

temp=[[0]*2 for _ in range(max(case)+1)]
temp[0]=[1,0]
temp[1]=[0,1]
for i in range(2,max(case)+1):
  temp[i][0]=temp[i-1][0]+temp[i-2][0]
  temp[i][1]=temp[i-1][1]+temp[i-2][1]

for j in case:
  print(temp[j][0],temp[j][1])