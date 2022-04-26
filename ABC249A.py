a,b,c,d,e,f,x = map(int,input().split())
y = 0
z = 0
for i in range(x):
  if i%(a+c)<a:
    y += b
  if i%(d+f)<d:
    z += e
if y>z:
  print("Takahashi")
elif y<z:
  print("Aoki")
else:
  print("Draw")