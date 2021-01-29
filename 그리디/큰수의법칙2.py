n,m,k=map(int, input().split())
data=list(map(int, input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

# 더 많아졌을 때를 생각해서 쉬운 계산식을 만들었음
# 가장 큰수를 더하는 횟수를 계산
count=int(m/(k+1))*k
count+=m%(k+1)

result=0
result+=(count)*first
result+=(m-count)*second

print(result)
