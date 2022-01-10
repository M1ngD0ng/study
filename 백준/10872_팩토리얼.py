N = int(input())
answer=1
def A(num):
  global answer
  if num==1:
    print(answer)
  elif num==0:
    print(1)
  else:
    answer=answer*num
    A(num-1)
A(N)