"""
問題文
今日の曜日を表す文字列 S が与えられます。
S は SUN,MON,TUE,WED,THU,FRI,SAT のいずれかであり、それぞれ日曜日、月曜日、火曜日、水曜日、木曜日、金曜日、土曜日を表します。
次の日曜日 (あす以降) が何日後か求めてください。
"""

s = input()
if s == "SUN":print(7)
elif s == "MON":print(6)
elif s == "TUE":print(5)
elif s == "WED":print(4)
elif s == "THU":print(3)
elif s == "FRI":print(2)
else:print(1)

#別解
s = input()
a = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
ans = 7-a.index(s)
print(ans)

#別解
S = input()
l = {
    'SUN': 7,
    'MON': 6,
    'TUE': 5,
    'WED': 4,
    'THU': 3,
    'FRI': 2,
    'SAT': 1
}
print(l[S])