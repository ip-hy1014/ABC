s = input()
l = ["0","1","2","3","4","5","6","7","8","9"]
for i in s:
  l.remove(i)
print(*l)