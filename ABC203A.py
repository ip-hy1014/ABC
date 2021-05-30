a,b,c = sorted(map(int, input().split()))
if a == b == c:
  print(a)
elif a != b != c:
  print(0)
elif a == b != c:
  print(c)
else:
  print(a)