n,k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(k):
  a.pop(0)
  a = a + [0]
print(*a)