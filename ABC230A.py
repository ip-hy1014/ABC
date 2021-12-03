n = int(input())
l = len(str(n))
if n<=41:
  if l==1:
    print("AGC"+"00"+str(n))
  elif l==2:
    print("AGC"+"0"+str(n))
else:
  print("AGC"+"0"+str(n+1))

#別解
n = int(input())
if n<=41:
  print("AGC"+str(n).zfill(3))
else:
  print("AGC"+str(n+1).zfill(3))