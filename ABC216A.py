n = float(input())
n_a = n*10
m = n_a%10
n_i = int(n)
n_s = str(n_i)
if 0<=m<=2:
	print(n_s+"-")
elif 3<=m<=6:
	print(n_s)
else:
	print(n_s+"+")