"""
問題文
A, B, C からなる長さ N の文字列 S と、1 以上 N 以下の整数 K が与えられます。
文字列 S の K 文字目を小文字に書き換え、新しくできた S を出力してください。
"""

n,k = map(int, input().split())
s = input()
print(s[:k-1]+s[k-1].lower()+s[k:])