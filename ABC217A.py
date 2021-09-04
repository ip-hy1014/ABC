l = list(input().split())
l_s = sorted(l)
if l[0] == l_s[0]:
  print("Yes")
else:
  print("No")

#別解
s,t = input().split()
print("Yes" if s<t else "No")
