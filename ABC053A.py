"""
問題文
すめけくんは現在のレートが 1200 未満ならば AtCoder Beginner Contest (ABC) に、そうでなければ AtCoder Regular Contest (ARC) に参加することにしました。
すめけくんの現在のレート x が与えられます。すめけくんが参加するコンテストが ABC ならば ABC と、そうでなければ ARC と出力してください。
"""

print("ABC" if int(input())<1200 else "ARC")