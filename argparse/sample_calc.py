import argparse
import contextlib

def cmd_add(args):
    return args.x + args.y

def cmd_sub(args):
    return args.x - args.y

def cmd_mul(args):
    return args.x * args.y

def cmd_div(args):
    try:
        return args.x / args.y
    except ZeroDivisionError:
        print("ゼロ除算はできません")
        exit()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="説明文")
    subparsers= parser.add_subparsers()

    parser_add = subparsers.add_parser('add', help='加算処理')
    parser_add.add_argument('x', help='', type=int)
    parser_add.add_argument('y', help='', type=int)
    parser_add.set_defaults(handler=cmd_add)

    parser_sub = subparsers.add_parser('sub', help='減算処理')
    parser_sub.add_argument('x', help='', type=int)
    parser_sub.add_argument('y', help='', type=int)
    parser_sub.set_defaults(handler=cmd_sub)
    
    parser_mul = subparsers.add_parser('mul', help='乗算処理')
    parser_mul.add_argument('x', help='', type=int)
    parser_mul.add_argument('y', help='', type=int)
    parser_mul.set_defaults(handler=cmd_mul)

    parser_div = subparsers.add_parser('div', help='除算処理')
    parser_div.add_argument('x', help='', type=int)
    parser_div.add_argument('y', help='', type=int)
    parser_div.set_defaults(handler=cmd_div)

    parser.add_argument('-o', '--output', help='ファイル出力', type=argparse.FileType("w"), default='-')

    args = parser.parse_args()

    if hasattr(args, 'handler'):
        result = args.handler(args)
        print(result)
        with contextlib.closing(args.output) as f:
            f.write(result)
    else:
        parser.print_help()
    
        