n = int(input())
s = input()
ans = "Yes"
for i in range(1,len(s)):
  if s[i]==s[i-1]:
    ans = "No"
print(ans)