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

# 元の記事: The Hitchhiker's Guide to Python

- 原文
  https://python-guideja.readthedocs.io/ja/latest/writing/structure.html
- 日本語訳
  https://python-guideja.readthedocs.io/ja/latest/writing/structure.html
