import math
n = int(input())
m = 1.08
if math.floor(n*m)<206:
  print("Yay!")
elif math.floor(n*m)==206:
  print("so-so")
else:
  print(":(")