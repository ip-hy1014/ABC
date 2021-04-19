"""
問題文
整数 n に対して、 n を十進法で表したときの各桁の和を S(n) で表すことにします。
例えば、S(123)=1+2+3=6 です。
2 つの 3 桁の整数 A,B が与えられます。
S(A) と S(B) のうち大きい方の値を求めてください。

出力
S(A) と S(B) のうち大きい方の値を出力せよ。
S(A) と S(B) が等しい場合は、S(A) を出力せよ。
"""

A, B = input().split()
a = sum(map(int, A))
b = sum(map(int, B))
print(a if a > b else b)

#別解
A, B = input().split()
a, b = 0, 0

for x, y in zip(A, B):
    a += int(x)
    b += int(y)

print(max(a, b))

"""
map関数を使用して、sum(map(int, 整数の文字列データ))で数字和を求めることができる。
"""