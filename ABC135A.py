"""
問題文
相違なる整数 A, B があります。
|A−K|=|B−K| となるような整数 K を出力してください。
そのような整数が存在しなければ、代わりに IMPOSSIBLE を出力してください。
"""

a,b = map(int, input().split())
print("IMPOSSIBLE" if (a+b)%2==1 else (a+b)//2)