"""
問題文
整数 a,b,c,d が与えられます。
a≤x≤b, c≤y≤d となるように整数 x,y を選ぶとき、 x−y の最大値を求めてください。

制約
入力は全て整数
−100≤a≤b≤100
−100≤c≤d≤100
"""

a, b = map(int, input().split())
c, d = map(int, input().split())
print(b - c)

"""
x−y を最大にしたい.そのために,x をできるだけ大きく,y をできるだけ小さくしたい.
a≤x≤b なので,x=b
c≤y≤d なので,y=c
つまり,b−c
"""
