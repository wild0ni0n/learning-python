# pipenv の設定

## pipenv とは

プロジェクト毎のパッケージ管理や仮想環境の構築を簡単に自動で行ってくれるツールらしい

- pip と venv を連携して動作させてくれる
- `requirements.txt`の代わりに`Pipfile`および`Pipfile.lock`を使う
- 依存関係が分かりやすい(例として `$ pipenv graph`)
- `.env` ファイルを読み込むことで、開発フローの効率化

https://pipenv-ja.readthedocs.io/ja/translate-ja/

## インストール

> \$ pip install pipenv

## 初期化

> \$ pipenv --python [バージョン]

> \$ pipenv --python 3.8

## PIPENV_VENV_IN_PROJECT 環境変数の設定

デフォルト設定で`pipenv install`を行うと、`~/.local/share/virtualenvs/`の下に仮想環境を作る。
実際に使う上では `./.venv` だったり`~/.venv` などと、仮想環境の場所を変えたいことがよくある。

### `$WORKON_HOME`: 仮想環境の親ディレクトリを変える

(linux)

`$ export WORKON_HOME=~/.venvs`

(windows cmd)

`set WORKON_HOME=~/.venvs`

(widndows PS )

`[system.environment]::SetEnvironmentVariable("WORKON_HOME","~/.venvs")`

### `$PIPENV_VENV_IN_PROJECT`: プロジェクトの直下に仮想環境を作る

(linux)

`$ export PIPENV_VENV_IN_PROJECT=true`

(windows cmd)

`set PIPENV_VENV_IN_PROJECT=true`

(windows PS)

`[system.environment]::SetEnvironmentVariable("PIPENV_VENV_IN_PROJECT","true")`

## プロジェクト環境の作成

> $ pipenv install
> $ ls
> .vscode
> Pipfile
> Pipfile.lock

# vscode の設定

## 拡張機能の設定

recommendations に設定しおくことで、このフォルダを vscode で開くとインストールの案内が表示される。

.vscode/extensions.json

```json
{
  "recommendations": ["ms-python.python"]
}
```

## python 拡張の設定

linter の設定や型チェックの設定

.vscode/settings.json

```json
{
  "python.venvPath": ".venv",
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": ["--max-line-length", "88"],
  "python.linting.mypyEnabled": true,
  "python.formatting.provider": "black",
  "python.unitTest.unittestEnabled": true,
  "python.unitTest.unittestArgs": ["discover", "test"],
  "editor.formatOnSave": true,
  "python.linting.lintOnSave": true,
  "git.ignoreLimitWarning": true
}
```

### 補足: lint, linter とは

lint とは、コンパイラやインタプリタよりも厳しくソースコードをチェックするプログラム
linter とは、lint を行うプログラムのこと。

### 補足: flake8 とは

python の文法チェックツールの 1 つ。
pep8, pyflakes, mccabe をラッピングしているらしい。

### 補足: mypy とは

python の静的型チェックツールの一つ。
型アノテーションを追加すると、mypy は型チェックを行ってくれる。

### 補足: black とは

コードフォーマッタの一つ。他にも autopep8, yapf 等が対応しているが、black が人気らしい。

### 補足: unittest とは

python の単体テストツールの一つ。unittest は標準のツール。

# .gitignore の用意

以下のひな型を使う

https://github.com/github/gitignore/blob/master/Python.gitignore

> \$ wget https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -O .gitignore

# パッケージのインストール

pipenv をつかってパッケージ管理を行う。
pip を直接使う場合だと、requirements.txt の更新を忘れたり、仮想環境を作るのを忘れて関係ないパッケージまで管理されてしまうといったことを防ぐことができる。

vscode で設定した black, flake8, mypy を開発用パッケージとして入れる。

> $ pipenv install --dev flake8 mypy
> $ pipenv install --dev --pre black

Pipfile の中身と Pipfile.lock の中身が更新される。

## Pipfile，Pipfile.lock から環境の再現

既に誰かが環境を作成し `Pipfile` を公開している場合、他のメンバーも簡単に環境を作成することができる

`Pipfile` を使って再現する場合

> $ pipenv install
> $ pipenv install --dev # 開発環境パッケージもインストールしたい場合

`Pipfile.lock` を使って再現する場合

> $ pipenv sync
> $ pipenv sync --dev # 開発環境パッケージをインストールしたい場合

# 参考

https://qiita.com/shibukawa/items/1650724daf117fad6ccd

https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a
