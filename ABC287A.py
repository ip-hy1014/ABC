n = int(input())
s = [input() for _ in range(n)]
f = s.count("For")
a = s.count("Against")
print("Yes" if f>=n//2+1 else "No")