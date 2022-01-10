import sys

T=int(input())
for _ in range(T):
  data=sys.stdin.readline().rstrip()
  A,B=map(int,data.split())
  print(A+B)