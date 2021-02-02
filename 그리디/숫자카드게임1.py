# 2021/02/02에 푼 문제
# p.96의 숫자 카드 게임 문제 _ 내 풀이
# 결과는 제대로지만 min(), max() 함수를 사용하지 않아서 코드가 너무 길다.

n,m=map(int, input().split())

min=0
max=0

for i in range(n):
  data=list(map(int,input().split()))
  data.sort()
  min=data[0]
  for j in range(m):
    if min>data[j]:
      min=data[j]
  if max<min:
    max=min

print(max)
