s = input()[::-1]
if "a" in s:
  print(len(s)-s.index("a"))
else:
  print(-1)