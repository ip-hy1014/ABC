from collections import Counter
a = list(map(int,input().split()))
c = Counter(a)
x = c.most_common()[0][1]
y = c.most_common()[1][1]
if x==3 and y==2:
  print("Yes")
else:
  print("No")