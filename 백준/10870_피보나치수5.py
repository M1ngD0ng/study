N = int(input())

def Fibo(num):
  if num==0:
    return 0
  elif num==1:
    return 1
  return Fibo(num-1)+Fibo(num-2)
  
print(Fibo(N))