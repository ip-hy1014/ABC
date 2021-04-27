"""
問題文
高橋君は九九を覚えたので、1 以上 9 以下の 2 つの整数の積を計算することができます。それ以外の計算はできません。
2 つの整数 A, B が与えられます。
高橋君が A×B を計算できるならその結果を、できないなら代わりに -1 を出力してください。
"""

a,b = map(int, input().split())
if a < 10 and b < 10:
  print(a*b)
else:
  print(-1)