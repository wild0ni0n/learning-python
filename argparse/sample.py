import argparse

def setup_argparse():
    parser = argparse.ArgumentParser(
        description="説明文",
        epilog="追加の説明文"
    )
    parser.add_argument("require", help="位置引数")
    parser.add_argument("-o", "--option", help="オプション引数")
    
    subparsers= parser.add_subparsers()
    parser_add = subparsers.add_parser('sub', help='サブコマンド')
    parser_add.add_argument('subrequire', help='サブコマンドの位置引数')
    parser_add.add_argument('-s','--sub-option', help='サブコマンドのオプション変数')
    
    parser_add = subparsers.add_parser('sub2', help='サブコマンド2')


    return parser.parse_args()

def main():
    args = setup_argparse()
    print(args)

if __name__ == "__main__":
    main()