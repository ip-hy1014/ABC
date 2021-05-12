"""
問題文
joisinoお姉ちゃんは、A op B という式の値を計算したいと思っています。 ここで、A,B は整数で、op は、+ または - の記号です。
あなたの仕事は、joisinoお姉ちゃんの代わりにこれを求めるプログラムを作ることです。
"""

a,op,b = input().split()
print(int(a)+int(b) if op=="+" else int(a)-int(b))

#別解
print(eval(input()))