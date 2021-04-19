"""
問題文
2×2 行列 A=[ab
            cd]
 が与えられます。
A の行列式は ad−bc で求められます。
A の行列式を求めてください。
"""

a, b = map(int, input().split())
c, d = map(int, input().split())
print(a*d-b*c)