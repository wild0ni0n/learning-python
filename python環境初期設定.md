# pipenvの設定
## pipenvとは
プロジェクト毎のパッケージ管理や仮想環境の構築を簡単に自動で行ってくれるツールらしい
* pipとvenvを連携して動作させてくれる
* requirements.txtの代わりにPipfileおよびPipfile.lockを使う
* 依存関係が分かりやすい(例として $ pipenv graph)
* .envファイルを読み込むことで、開発フローの効率化

https://pipenv-ja.readthedocs.io/ja/translate-ja/


## インストール
> $ pip install pipenv

## 初期化

> $ pipenv --python [バージョン]

> $ pipenv --python 3.8

## PIPENV_VENV_IN_PROJECT環境変数の設定
デフォルト設定でpipenv installを行うと、~/.local/share/virtualenvs/の下に仮想環境を作る。
実際に使う上では ./.venv だったり~/.venv などと、仮想環境の場所を変えたいことがよくある。

### $WORKON_HOME: 仮想環境の親ディレクトリを変える

(linux)
> $ export WORKON_HOME=~/.venvs

(windows cmd)
> set WORKON_HOME=~/.venvs

(widndows PS )
> [System.Environment]::SetEnvironmentVariable("WORKON_HOME","~/.venvs")

### $PIPENV_VENV_IN_PROJECT: プロジェクトの直下に仮想環境を作る

(linux)
> $ export PIPENV_VENV_IN_PROJECT=true

(windows cmd)
> set PIPENV_VENV_IN_PROJECT=true

(windows PS)
> [System.Environment]::SetEnvironmentVariable("PIPENV_VENV_IN_PROJECT","true")

## プロジェクト環境の作成
> $ pipenv install
> $ ls
>.vscode
>Pipfile
>Pipfile.lock

# vscodeの設定
## 拡張機能の設定
recommendationsに設定しおくことで、このフォルダをvscodeで開くとインストールの案内が表示される。

.vscode/extensions.json
```json
{
    "recommendations": [
        "ms-python.python"
    ]
}
```

## python拡張の設定
linterの設定や型チェックの設定

.vscode/settings.json
```json
{
    "python.venvPath": ".venv",
    "python.pythonPath": "${workspaceFolder}/.venv/bin/python",
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": ["--max-line-length", "88"],
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "python.unitTest.unittestEnabled": true,
    "python.unitTest.unittestArgs": [
      "discover", "test"
    ],
    "editor.formatOnSave": true,
    "python.linting.lintOnSave": true,
    "git.ignoreLimitWarning": true
}
```

### 補足: lint, linterとは
lintとは、コンパイラやインタプリタよりも厳しくソースコードをチェックするプログラム
linterとは、lintを行うプログラムのこと。

### 補足: flake8とは
pythonの文法チェックツールの1つ。
pep8, pyflakes, mccabeをラッピングしているらしい。

### 補足: mypyとは
pythonの静的型チェックツールの一つ。
型アノテーションを追加すると、mypyは型チェックを行ってくれる。

### 補足: blackとは
コードフォーマッタの一つ。他にもautopep8, yapf等が対応しているが、blackが人気らしい。

### 補足: unittestとは
pythonの単体テストツールの一つ。unittestは標準のツール。

# .gitignoreの用意
以下のひな型を使う
https://github.com/github/gitignore/blob/master/Python.gitignore

> $ wget https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -O .gitignore

# パッケージのインストール
pipenvをつかってパッケージ管理を行う。
pipを直接使う場合だと、requirements.txtの更新を忘れたり、仮想環境を作るのを忘れて関係ないパッケージまで管理されてしまうといったことを防ぐことができる。

vscodeで設定したblack, flake8, mypyを開発用パッケージとして入れる。

> $ pipenv install --dev flake8 mypy
> $ pipenv install --dev --pre black

Pipfileの中身とPipfile.lockの中身が更新される。

## Pipfile，Pipfile.lockから環境の再現
既に誰かが環境を作成しPipfileを公開している場合、他のメンバーも簡単に環境を作成することができる

Pipfileを使って再現する場合
> $ pipenv install
> $ pipenv install --dev  # 開発環境パッケージもインストールしたい場合

Pipfile.lockを使って再現する場合
> $ pipenv sync
> $ pipenv sync --dev  # 開発環境パッケージをインストールしたい場合


# 参考
https://qiita.com/shibukawa/items/1650724daf117fad6ccd
https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a