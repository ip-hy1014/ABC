"""
問題文
3 つ組の数について、ある 2 つが等しく、残りの 1 つがそれらと異なるとき、その 3 つ組を「かわいそう」であるといいます。
3 つの整数 A,B,C が与えられるので、この 3 つ組がかわいそうであれば Yes を、そうでなければ No を出力してください。
"""

a,b,c = map(int, input().split())
if a == b and a != c and b != c:
  print("Yes")
elif b == c and a != b and a != c:
  print("Yes")
elif a == c and b != a and b != c:
  print("Yes")
else:
  print("No")

#別解
a = list(map(int,input().split()))
print("Yes" if len(set(a))==2 else "No") #set()で重複する要素を省く