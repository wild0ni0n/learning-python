import argparse

def com():
    return True

def com2():
    return True

parser = argparse.ArgumentParser()
parser.add_argument("-a","--addr", default="0.0.0.0", help="サーバのIPアドレスを指定します")
parser.add_argument("-p","--port", default="80", help="サーバのポート番号を指定します")

parser.add_argument("mode", help="Chatoyancyのモードを指定します")
subparsers = parser.add_subparsers()

# カウントアップモード
parser_cnt = subparsers.add_parser("count", help="カウントアップの値を出力するモードにします")
parser_cnt.add_argument("-i", "--init", type=int, default=0, help="初期値を指定します")
parser_cnt.add_argument("-l", "--limit", type=int, default=None, help="上限値を指定します。上限を超えた場合プログラムを終了します")

# 最小最大指定モード
parser_mm = subparsers.add_parser("minmax", help="指定した最小値と最大値の範囲で乱数を出力するモードにします。デフォルトは0-1000です。")
parser_mm.add_argument("-s", "--min", type=int, default=0, help="最小値を指定します")
parser_mm.add_argument("-e", "--max", type=int, default=1000, help="最大値を指定します")

# 桁数指定モード
parser_dig = subparsers.add_parser("digit", help="指定した桁数の乱数を出力するモードにします。デフォルトは10です。")
parser_dig.add_argument("-d", "--digit", type=int, default=10, help="桁数を指定します")

# 文字列指定モード
parser_pass = subparsers.add_parser("alph", help="ランダムな文字列を出力するモードにします。デフォルトは10です。")
parser_pass.add_argument("-l", "--len", "--length", type=int, default=10, help="文字数を指定します")

# ファイル指定モード
parser_file = subparsers.add_parser("file", help="指定したパスの内容を出力するモードにします")
parser_file.add_argument("file", type=argparse.FileType("r"), help="読み込先のパスを指定します")

args = parser.parse_args()
print(args)