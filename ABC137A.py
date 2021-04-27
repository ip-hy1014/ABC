"""
問題文
整数 A, B があります。
A+B, A−B, A×B の中で最大の数を出力してください。
"""

a,b = map(int, input().split())
print(max(a+b, a-b, a*b))