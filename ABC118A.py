"""
問題文
正整数 A,B が与えられます。
A が B の約数なら A+B を、そうでなければ B−A を出力してください。
"""

a,b = map(int, input().split())
print(a+b if b%a==0 else b-a)