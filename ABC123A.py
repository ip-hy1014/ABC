"""
問題文
AtCoder 市には、5 つのアンテナが一直線上に並んでいます。これらは、西から順にアンテナ A,B,C,D,E と名付けられており、
それぞれの座標は a,b,c,d,e です。
2 つのアンテナ間の距離が k 以下であれば直接通信ができ、k より大きいと直接通信ができません。
さて、直接 通信ができないアンテナの組が存在するかどうか判定してください。
ただし、座標 p と座標 q (p<q) のアンテナ間の距離は q−p であるとします。

直接 通信ができないアンテナの組が存在する場合は :(、存在しない場合は Yay! と出力せよ。
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
print("Yay!" if e-a<=k else ":(")

#別解
l = [int(input()) for _ in range(5)]
k = int(input())
print('Yay!' if max(l) - min(l) <= k else ':(')