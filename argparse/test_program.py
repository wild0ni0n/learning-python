import argparse

parser = argparse.ArgumentParser(description="説明A")
parser.add_argument("integers", metavar='N', type=int, nargs='+', help="整数型のヘルプメッセージ")
parser.add_argument("--sum", dest="accumulate", action="store_const", const=sum, default=max, help="sumのヘルプメッセージ")
args = parser.parse_args()
print(args.accumulate(args.integers))