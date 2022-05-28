a,b,c = map(int,input().split())
l = [a,b,c]
l.sort()
print("Yes" if l[1]==b else "No")