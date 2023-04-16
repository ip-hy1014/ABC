# 入力の受け取り
N = int(input())  # 面接官の人数
S = input()  # 面接官の評価

# 条件判定
if 'o' in S  and 'x' not in S:
    # 「良」の評価があるか、全ての評価が「可」の場合
    print("Yes")
else:
    # 「良」の評価がなく、かつ「不可」の評価もある場合
    print("No")