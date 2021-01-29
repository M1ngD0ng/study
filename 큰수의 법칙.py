# 2021/01/29에 푼 문제
# p.92의 큰 수의 법칙 문제

# 공백 구분하여 입력받기
n,m,k=map(int, input().split())
data=list(map(int, input().split()))

# 일단 정렬하기
data.sort()

# 가장 큰 수 K번 더하고 두번째로 큰 수 한번 더하는 연산 반복하면 되니까 일단 큰거 2개 저장하기
first=data[n-1]
second=data[n-2]

result=0

# 무한 루프 돌리기
while True:
  # 가장 큰 수를 K번만 더함
  for i in range (k):
    if m==0:
      break
    result+=first
    m-=1
  if m==0:
    break
  # 두 번째로 큰 수를 1번 더함
  result+=second
  m-=1

print(result)
