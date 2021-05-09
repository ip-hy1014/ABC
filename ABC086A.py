#シカのAtCoDeerくんは二つの正整数a,bを見つけました。aとbの積が偶数か奇数か判定してください。

a, b = map(int, input().split())
print("Even" if a*b % 2 == 0 else "Odd")

"""
標準入力はinput関数で入力する（文字列(str)型で入力される）。
標準入力から整数を得たい場合、整数(int)型int(input())に変換する。
標準入力から浮動小数点数を得たい場合、浮動小数点数(float)型float(input())に変換する。
標準入力から得た文字列を区切りたい場合、split関数を用いてinput().split("区切り文字")と使用する。
split関数で区切り文字を指定しない場合input().split()、半角スペース で区切られる。
複数列の整数の標準入力を複数の変数に格納したい場合、map関数を用いてmap(int, input().split())と使用する。
"""