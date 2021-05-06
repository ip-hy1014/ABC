"""
問題文
N 両編成の列車があります。
この列車の前から i 両目は、後ろから何両目でしょうか？
"""

n,i = map(int, input().split())
print(n-i+1)