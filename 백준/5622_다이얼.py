data=input()
asc=[]
for s in str(data):
  asc.append(ord(s))
cnt=0
for n in asc:
  if 64<n<68:
    cnt=cnt+3
  elif 67<n<71:
    cnt=cnt+4
  elif 70<n<74:
    cnt=cnt+5
  elif 73<n<77:
    cnt=cnt+6
  elif 76<n<80:
    cnt=cnt+7
  elif 79<n<84:
    cnt=cnt+8
  elif 83<n<87:
    cnt=cnt+9
  elif 86<n<91:
    cnt=cnt+10

print(cnt)