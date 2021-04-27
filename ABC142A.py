"""
問題文
整数 N が与えられます。
高橋君は、N 以下の正整数の中から等確率で 1 つを選んで a とします。
このとき、a が奇数である確率を答えてください。
"""

n = int(input())
if n % 2 == 0:
  print('{:.10g}'.format((n/2)/n))
else:
  print('{:.10g}'.format(((n+1)/2)/n))

#別解
n = int(input())
print((n + 1) // 2 / n)
