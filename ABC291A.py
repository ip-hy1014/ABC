s = input()
for i in s:
  if i.isupper():
    print(s.index(i)+1)
    exit()