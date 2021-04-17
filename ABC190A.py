"""
問題文
高橋くんと青木くんがゲームを行います。
はじめ、高橋くんは A 個、青木くんは B 個のアメを持っています。
C=0 ならば高橋くんが先手、C=1 ならば青木くんが先手で、高橋くんと青木くんは以下の操作を交互に繰り返します。
自分の持っているアメを 1 個食べる。
先に操作を行えなくなった者の負けです。どちらが勝つでしょうか？

出力
高橋くんが勝つならば Takahashi を、青木くんが勝つならば Aoki を出力せよ。
"""

A, B, C = map(int, input().split())
if C == 0:
  if A>B:
    print("Takahashi")
  else:
    print("Aoki")
else:
  if A>=B:
    print("Takahashi")
  else:
    print("Aoki")
