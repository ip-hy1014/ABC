a = input()
b = int(a[1]+a[2]+a[0])
c = int(a[2]+a[0]+a[1])
print(int(a)+b+c)

#別解
n = int(input())
s = str(n)
l = sum(list(map(int,s)))
print(l*111)
