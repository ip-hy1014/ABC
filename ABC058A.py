"""
問題文
3 本の柱が等間隔に並んでいます。柱の高さは左から順に a メートル, b メートル, c メートル です。
柱の先端が同一直線上に並んでいる時、つまり b−a=c−b を満たしているとき、 この柱の並び方を美しいと呼びます。
柱の並び方が美しいかどうかを判定してください。

出力
柱の並び方が美しい場合 YES を、そうでない場合 NO を 1 行に出力せよ。
"""

a,b,c = map(int, input().split())
print("YES" if b-a==c-b else "NO")