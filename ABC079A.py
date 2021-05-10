"""
問題文
1118 のような、3 つ以上の同じ数字が連続して並んだ 4 桁の整数を 良い整数 とします。
4 桁の整数 N が与えられるので、N が 良い整数 かどうかを答えてください。

出力
N が 良い整数 ならば Yes を、そうでなければ No を出力せよ。
"""

n = input()
if n[0]==n[1]==n[2]:
  print("Yes")
elif n[1]==n[2]==n[3]:
  print("Yes")
else:
  print("No")

#別解
a,b,c,d=input()
print("Yes" if a==b==c or b==c==d else "No")