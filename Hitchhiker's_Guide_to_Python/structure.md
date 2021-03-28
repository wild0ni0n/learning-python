# リポジトリの構造

## サンプルリポジトリ

- README.rst
- LICENSE
- setup.py
- requirements.txt
- sample/**init**.py
- sample/core.py
- sample/helpers.py
- docs/conf.py
- docs/index.rst
- tests/test_basic.py
- tests/test_advanced.py

https://github.com/kennethreitz/samplemod

### モジュール

作成したモジュールが複数で構成されているなら、`./sample/`ディレクトリを作成して、モジュールパッケージをまとめる。
もし単体で構成されている場合には、リポジトリのルートに直接置いてもよい。
そうでない場合は、`src`や`python`といった曖昧なサブディレクトリに置かないこと。

### requirements ファイル

パッケージの依存関係の解決、モジュールのテスト、ビルドを行うために必要。

依存関係がない場合や、`setup.py`を介して開発環境を設定する場合には、requirements.txt は不要。

### Makefile

プロジェクトのタスクを定義するための便利なツールとして用意しておく。
C 言語で書かれている必要はない。

サンプル Makefile

```
init:
    pip install -r requirements.txt

test:
    py.test tests

.PHONY: init test
```

requests には Makefile が置いてあることが分かる。

- requests
  - https://github.com/psf/requests/blob/master/Makefile

しかし、flask や duango、werkzeug などには Makefile が置いてないので、一般化されたものでもないらしい。

# コード構造

構造化が整っていないプロジェクトの例

- 複数の乱雑な循環依存関係
  - 循環するようなインポートは止めようって話
- 隠れた結合
  - ある機能を修正したとき、その機能とは無関係な箇所のテストケースが何度も失敗する場合、密結合である可能性がある
- グローバルな状態やコンテキストの大量使用
  - グローバル領域を大量に利用するような書き方は止めようって話
- スパゲッティコード
  - 多数のネストされた if 節、多数のコピペコード、セグメンテーション違反なループなど
- ラビオリコード
  - 大量に類似した小さいクラスやオブジェクトで構成されているコードなど。

# モジュール

スタイルガイドに一致するようなモジュール名を心掛ける

- 小文字にする
- ドットや疑問符などの記号は使用しないこと

悪い例: `my.spam.py`
悪い例: `my_spam.py` # インポートできるものの、これは記号を使っており慣習的ではない

インポートされたモジュールは、モジュール内のトップレベルのステートメントが実行される。
関数やクラスの定義は、モジュールの辞書に格納される。

`import * `や`from hoge import *`は、インポートによる影響範囲が広くなり、難読性があがるため使用を控えたほうがよい。
その他にも依存関係を収束させにくいといったデメリットがある。

# パッケージ

`__init__.py`ファイルを持つディレクトリは、Python パッケージと見なす。

ディレクトリ`pack/`に配置された`modu.py`は、`import pack.modu` というステートメントでインポートされる。

`__init__.py`は空のままにしておくのが良い習慣である。

# オブジェクト指向プログラミング

Python ではすべてがオブジェクトであり、オブジェクトとして扱うことが出来る。
関数、クラス、文字列、型などもオブジェクトとして扱えるので、型を持つことや関数の引数として渡すことができることやメソッドやプロパティを持たせることもできる。

Java と異なる点は、Python のオブジェクト指向プログラミングでは主なプログラミングパラダイムを課さない。

オブジェクト指向を必要としないとき、オブジェクト指向を使用しないということもできる。

# デコレータ

デコレータとは、関数やメソッドをラップする関数やクラスのこと。
`@デコレータ構文`を使用せずに手動に行う事もできるが、構文を利用したほうが明確である。

```python
def foo():
    # do something

def decorator(func):
    # manipulate func
    return func

foo = decorator(foo) # これは手動によるデコレート

@decorator
def bar():
    # do domething
# bar()関数はデコレートされている
```

# コンテキストマネージャ

with 文を使って文脈を開始すると同時に、 with ブロック内のすべてのコードを完了したときに呼び出し可能なものを実行する。

ファイル操作でよく利用され、with 文を使って`open`されたファイルは、with ブロックから抜けるときに`close`が呼び出される。
クラスを使用して実装する方法とジェネレータを使用する方法がある。

クラスを使用して実装する

```python
class CustomOpen(object):
    def __init__(self, filename):
      self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file') as f:
    contents = f.read()
```

インスタンス化されたあと`__enter__`メソッドが呼び出され、`as`の`f`に返り値が渡される。
with ブロックを抜けるときに`__exit__`が呼び出される。

ジェネレータを使用して実装する

```python
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file') as f:
    contents = f.read()
```

# 元の記事: The Hitchhiker's Guide to Python

- 原文
  https://docs.python-guide.org/writing/structure/
- 日本語訳
  https://python-guideja.readthedocs.io/ja/latest/writing/structure.html
