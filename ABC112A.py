"""
問題文
2020 年, AtCoder 社は年商 10 億円を超え, プログラミング教育にも手を出すようになった.
ある日行われたテストでは, 1 才児は Hello World を出力するプログラムを,
2 才児は整数 A, B を入力して A+B を出力するプログラムを書かなければならない.
高橋君はこのテストを受けているが, 突然自分が何才なのかが分からなくなってしまった.
そこで, 最初に自分の年齢 N (N は 1 または 2) を入力し, N=1 ならば Hello World と出力し, N=2 ならば A, B を入力して A+B を出力するプログラムを作ることにした.
高橋君に代わって, このようなプログラムを作りなさい.
"""

n = int(input())
if n == 1:
  print("Hello World")
else:
  a = int(input())
  b = int(input())
  print(a+b)

#別解
n = int(input())
if n == 1:
	print('Hello World')
else:
	print(int(input())+int(input()))