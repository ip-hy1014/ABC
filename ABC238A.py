n = int(input())
print("Yes" if 2**n>n**2 else "No")

#別解
import math
n = int(input())
l = math.log(n,2)
print("Yes" if n>2*l else "No")