n = int(input())
s = input().split()
ans = "No"
for i in s:
  if i in ["and", "not", "that", "the", "you"]:
    ans = "Yes"
print(ans)