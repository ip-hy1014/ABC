"""
問題文
2 つの正整数 a, b が与えられます。 a, b の平均値を x とします。
x の小数点以下を切り上げて得られる整数を出力してください。
"""

import math
a,b = map(int, input().split())
print(math.ceil((a+b)/2))

#別解
a, b = map(int, input().split())
print((a + b + 1) // 2)