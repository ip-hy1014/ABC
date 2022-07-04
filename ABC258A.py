n = int(input())
if n<60:
  print("21:"+str(n).zfill(2))
else:
  print("22:"+str(n-60).zfill(2))

#golf
n = int(input())
print(f"{21+n//60}:{n%60:02}")