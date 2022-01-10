N=int(input())

def cal(num):
  A=[]
  if int(num)<10:
    A.append(str('0'))
    A.append(str(num))
  else:
    for i in str(num):
      A.append(int(i))
  return A

def cal_sec_sum(num):
  lst=cal(num)
  sum=lst[0]+lst[1]
  B=cal(sum)
  return (lst[1],int(B[1]))

sec, sum=cal_sec_sum(N)
cnt=1
new=str(sec)+str(sum)
while True:
  sec,sum =cal_sec_sum(int(new))
  if int(new)==N:
    break
  cnt+=1
  new=int(str(sec)+str(sum))
print(cnt)