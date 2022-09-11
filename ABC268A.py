a = list(map(int,input().split()))
print(len(set(a)))

#golf
print(len({*input().split()}))
#iterableをsetに変換 → {*iterable}