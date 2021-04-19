"""
問題文
ReLU関数は以下のように定義されます。
x>=0→xを出力
x<0→0を出力
整数 x が与えられるので ReLU(x) を求めてください。
"""

x = int(input())
print(x if x>=0 else 0)

