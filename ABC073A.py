"""
問題文
今、日本は 9 月 9 日です。 二桁の整数 N が与えられるので、十進法で N に 9 が含まれるか答えてください。

出力
9 が含まれるとき Yes 、含まれないとき No を出力せよ。
"""

n = input()
print("Yes" if n[0]=="9" or n[1]=="9" else "No")

#別解
if "9" in input():
  print("Yes")
else:
  print("No")