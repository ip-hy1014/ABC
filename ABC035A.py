w,h = map(int, input().split())
if w*3==h*4:
	print("4:3")
else:
	print("16:9")

#別解
a,b = map(int, input().split())
print("4:3" if a/b==4/3 else "16:9")