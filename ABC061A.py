"""
問題文
3 つの整数 A,B,C が与えられます。
整数 C が A 以上 かつ B 以下であるかを判定してください。

出力
条件を満たす場合はYes、そうでない場合はNoを出力せよ。
"""

a,b,c = map(int, input().split())
print("Yes" if a<=c<=b else "No")