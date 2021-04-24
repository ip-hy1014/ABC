"""
整数 A,B,C が与えられます。
A^2+B^2<C^2 かを判定してください。
"""

a, b, c = map(int, input().split())
if (a**2)+(b**2)<c**2:
  print("Yes")
else:
  print("No")