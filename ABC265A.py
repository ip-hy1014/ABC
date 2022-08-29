x,y,n = map(int,input().split())
if 3*x<y:
  print(x*n)
else:
  a = n//3
  b = n%3
  print(a*y+b*x)