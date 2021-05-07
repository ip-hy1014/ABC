"""
問題文
数直線上にいるAさんとBさんとCさんがトランシーバーで会話をしようとしています。 Aさんは a [m] 地点、Bさんは b [m] 地点、Cさんは c [m] 地点にいます。
二人の人間は、距離が d [m] 以内のとき直接会話が出来ます。
AさんとCさんが直接的、あるいは間接的に会話ができるか判定してください。
ただしAさんとCさんが間接的に会話ができるとは、AさんとBさんが直接会話でき、かつBさんとCさんが直接会話できることを指します。

出力
会話できるなら Yes を, できないなら No を出力せよ。
"""

a,b,c,d = map(int, input().split())
if abs(a-b) <= d and abs(b-c) <= d:
  print("Yes")
elif abs(a-c) <= d:
  print("Yes")
else:
  print("No")

#別解
a,b,c,d=map(int,input().split())
print(["No","Yes"][abs(a-c)<=d or abs(a-b)<=d and abs(b-c)<=d])