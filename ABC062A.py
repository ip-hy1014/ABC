"""
問題文
すぬけ君は、1 から 12 までの整数を下図のようにグループ分けしました。
整数 x, y (1≤x<y≤12) が与えられるので、x, y が同一のグループに属しているか判定してください。

出力
x, y が同一のグループに属しているならば Yes を、そうでなければ No を出力せよ。
"""

l0 = list(map(int, input().split()))
l1 = [1,3,5,7,8,10,12]
l2 = [4,6,9,11]
if len(set(l0) & set(l1)) == 2:
  print("Yes")
elif len(set(l0) & set(l2)) == 2:
  print("Yes")
else:
  print("No")