"""
西暦 N 年は何世紀ですか？
"""

n = int(input())
if n % 100 == 0:
  print(n//100)
else:
  print(n//100+1)

#別解
n=int(input())
print((n-1)//100+1)