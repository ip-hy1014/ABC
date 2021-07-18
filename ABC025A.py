s = input()
n = int(input())
l = []
for i in s:
  for j in s:
    l.append(i+j)
l = sorted(l)
print(l[n-1])

#別解
import itertools
s = input()
n = int(input())
print(*list(itertools.product(s,repeat=2))[n-1],sep='')