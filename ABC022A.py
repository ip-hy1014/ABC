n,s,t = map(int,input().split())
w = 0
ans = 0
for _ in range(n):
  w += int(input())
  if s<= w <= t:
    ans += 1
print(ans)