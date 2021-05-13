"""
問題文
英小文字 c が与えられるので、c が母音であるか判定してください。ここで、英小文字のうち母音は a、e、i、o、uの 5 つです。

出力
c が母音であるとき、vowel と、そうでないとき consonant と出力せよ。
"""

c = input()
print("vowel" if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" else "consonant")

#別解
c = input()
print("vowel" if c in "aeiou" else "cosonant")