"""
問題文
長さ 3 の数列 A=(A1,A2,A3) が与えられます。
A を適切に並び替えて等差数列にすることはできますか？
即ち、A3−A2=A2−A1 を満たすように A を並び替えることはできますか？
"""

a,b,c = sorted(map(int, input().split()))
print("Yes" if c-b==b-a else "No")
