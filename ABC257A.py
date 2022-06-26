n,x = map(int,input().split())
ans = ""
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
  for j in range(n):
    ans += i
print(ans[x-1])