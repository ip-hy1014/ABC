"""
問題文
とある世界では、今日は 12 月 D 日です。
D=25 なら Christmas, D=24 なら Christmas Eve, D=23 なら Christmas Eve Eve, D=22 なら Christmas Eve Eve Eve と出力するプログラムを作ってください。
"""

d = int(input())
if d == 25:
  print("Christmas")
elif d == 24:
  print("Christmas Eve")
elif d == 23:
  print("Christmas Eve Eve")
else:
  print("Christmas Eve Eve Eve")

#別解
print("Christmas"+" Eve"*(25-int(input())))