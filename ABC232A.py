s = input()
a = int(s[0])
b = int(s[2])
print(a*b)

#別解
a,b = map(int,input().split("x"))
print(a*b)