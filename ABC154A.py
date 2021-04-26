"""
問題文
文字列 S の書かれたボールが A 個、文字列 T の書かれたボールが B 個あります。
高橋君は、文字列 U の書かれたボールを 1 個選んで捨てました。
文字列 S,T の書かれたボールがそれぞれ何個残っているか求めてください。
"""

s,t = input().split()
a,b = map(int, input().split())
u = input()
if s == u:
  print(a-1,b)
else:
  print(a,b-1)
