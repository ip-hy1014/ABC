"""
問題文
2 つの整数 A, B が与えられます。 A+B, A−B, A×B の中で最大の値を求めてください。
"""

a,b=map(int,input().split());print(max(a+b,a-b,a*b))