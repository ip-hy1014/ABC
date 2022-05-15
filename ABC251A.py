s = input()
l = len(s)
if l==1:
  print(s*6)
elif l==2:
  print(s*3)
else:
  print(s*2)

#golf
print((input()*6)[:6])
