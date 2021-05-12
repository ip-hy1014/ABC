"""
問題文
シカのAtCoDeerくんとTopCoDeerくんが「正直者か嘘つきか」ゲームをしています。 このゲームでは、正直者は常にほんとうのことを言い、嘘つきは常に嘘を言います。
文字 a と b が入力として与えられます。これらはそれぞれ H か D のどちらかです。
a=H のとき、AtCoDeerくんは正直者です。 a=D のとき、AtCoDeerくんは嘘つきです。
b=H のとき、AtCoDeerくんは「TopCoDeerくんは正直者だ」と発言しています。 b=D のとき、AtCoDeerくんは「TopCoDeerくんは嘘つきだ」と発言しています。
これらから判断して、TopCoDeerくんが正直者かどうか判定してください。

出力
TopCoDeerくんが正直者なら H を、嘘つきなら D を出力せよ。
"""

a,b = input().split()
print("H" if a==b else "D")