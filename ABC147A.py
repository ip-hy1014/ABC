"""
問題文
3 個の整数 A1, A2, A3 が与えられます。
A1+A2+A3 が 22 以上なら bust、21 以下なら win を出力してください。
"""

a1,a2,a3 = map(int, input().split())
print("win" if a1+a2+a3<=21 else "bust")