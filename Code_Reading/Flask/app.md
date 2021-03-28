# ファイル構成

src/flask 配下

- app.py
  - Flask のメインプログラム部分。
- blueprints.py
- cli.py
- config.py
- ctx.py
- debughelpers.py
- globals.py
- helpers.py
  - 便利な関数群や scaffold（と scaffold を継承するクラス）で利用する共通の関数をまとめている
  - mixin クラス
- logging.py
- scaffold.py
- sessions.py
- signals.py
- templating.py
- testing.py
- views.py
- wrappers.py

# app.py

## Flask class のヒアドキュメント

The flask object implements a WSGI application and acts as the central object.
It is passed the name of the module or package of the application.
Once it is created it will act as a central registry for the view functions, the URL rules, template configuration and much more.
The name of the package is used to resolve resources from inside the package or the folder the module is contained in depending on if the package parameter resolves to an actual python package (a folder with an :file:`__init__.py` file inside) or a standard module (just a `.py` file).
For more information about resource loading, see :func:`open_resource`.
Usually you create a :class:`Flask` instance in your main module or in the :file:`__init__.py` file of your package like this::

from flask import Flask
app = Flask(**name**)

.. admonition:: About the First Parameter

The idea of the first parameter is to give Flask an idea of what belongs to your application.
This name is used to find resources on the filesystem, can be used by extensions to improve debugging information and a lot more.
So it's important what you provide there.
If you are using a single module, `__name__` is always the correct value.
If you however are using a package, it's usually recommended to hardcode the name of your package there.
For example if your application is defined in :file:`yourapplication/app.py` you should create it with one of the two versions below::

app = Flask('yourapplication')
app = Flask(**name**.split('.')[0])

Why is that? The application will work even with `__name__`, thanks to how resources are looked up.
However it will make debugging more painful.
Certain extensions can make assumptions based on the import name of your application.
For example the Flask-SQLAlchemy extension will look for the code in your application that triggered an SQL query in debug mode.
If the import name is not properly set up, that debugging information is lost.
(For example it would only pick up SQL queries in `yourapplication.app` and not `yourapplication.views.frontend`)

## app.py heredoc(jp)

flask オブジェクトは WSGI アプリケーションを実装し、中心オブジェクト(central object)として動作します。
flask オブジェクトには、アプリケーションのモジュールやパッケージの名前が渡されます。
一度作成されると、ビュー関数、URL ルール、テンプレート設定などの中央レジストリとして動作します。
パッケージの名前は、実際の python パッケージ (フォルダ内に :file:`__init__.py` ファイルが入っているフォルダ) か標準モジュール (ただの `.py` ファイル) かに応じて、パッケージ内のリソースを解決するために使用されます。
リソースの読み込みについての詳細は:func:`open_resource`を参照してください。
通常、メインモジュールやパッケージの :file:`__init__.py` ファイルの中に :class:`Flask` インスタンスを以下のように作成します。

from flask import Flask
app = Flask(**name**)

.. 訓戒: 最初のパラメータについて

最初のパラメータのアイデアは、アプリケーションに属するアイデアを Flask に与えることです。
この名前は、ファイルシステム上のリソースを見つけるために使用され、デバッグ情報を改善するために拡張機能を使用することができます。
そのため、何を提供するかが重要です。
単一のモジュールを使っている場合は、`__name__` が常に正しい値となります。
しかし、パッケージを使用している場合は、パッケージの名前をハードコードすることを推奨します。
例えば、アプリケーションが :file:`yourapplication/app.py` で定義されている場合、以下の 2 つのバージョンのうちのいでずれかで作成する必要があります。

app = Flask('yourapplication')
app = Flask(**name**.split('.')[0])

アプリケーションは `__name__` であっても、リソースの検索方法のおかげで動作します。
しかし、これはデバッグを大変にします。
特定の拡張機能はアプリケーションのインポート名に基づいて処理されます。
例えば、Flask-SQLAlchemy 拡張機能は、デバッグモードで SQL クエリをトリガしたアプリケーションのコードを探索します。
インポート名が適切に設定されていない場合、デバッグ情報は失われます。
(例えば、`yourapplication.app`内の SQL クエリのみを検出し、`yourapplication.views.frontend`内の SQL クエリは検出しません)

---

Flask クラスのメンバー変数

```python
request_class = Request
response_class = Response
jinja_environment = Environment
app_ctx_globals_class = \_AppCtxGlobals
config_class = Config
testing = ConfigAttribute("TESTING")
secret_key = ConfigAttribute("SECRET_KEY")
session_cookie_name = ConfigAttribute("SESSION_COOKIE_NAME")
permanent_session_lifetime = ConfigAttribute(
    "PERMANENT_SESSION_LIFETIME", get_converter=\_make_timedelta
)
send_file_max_age_default = ConfigAttribute(
    "SEND_FILE_MAX_AGE_DEFAULT", get_converter=\_make_timedelta
)
use_x_sendfile = ConfigAttribute("USE_X_SENDFILE")
json_encoder = json.JSONEncoder
json_decoder = json.JSONDecoder
jinja_options = {"extensions": ["jinja2.ext.autoescape", "jinja2.ext.with*"]}
default_config = ImmutableDict(
{
    "ENV": None,
    "DEBUG": None,
    "TESTING": False,
    "PROPAGATE_EXCEPTIONS": None,
    "PRESERVE_CONTEXT_ON_EXCEPTION": None,
    "SECRET_KEY": None,
    "PERMANENT_SESSION_LIFETIME": timedelta(days=31),
    "USE_X_SENDFILE": False,
    "SERVER_NAME": None,
    "APPLICATION_ROOT": "/",
    "SESSION_COOKIE_NAME": "session",
    "SESSION_COOKIE_DOMAIN": None,
    "SESSION_COOKIE_PATH": None,
    "SESSION_COOKIE_HTTPONLY": True,
    "SESSION_COOKIE_SECURE": False,
    "SESSION_COOKIE_SAMESITE": None,
    "SESSION_REFRESH_EACH_REQUEST": True,
    "MAX_CONTENT_LENGTH": None,
    "SEND_FILE_MAX_AGE_DEFAULT": timedelta(hours=12),
    "TRAP_BAD_REQUEST_ERRORS": None,
    "TRAP_HTTP_EXCEPTIONS": False,
    "EXPLAIN_TEMPLATE_LOADING": False,
    "PREFERRED_URL_SCHEME": "http",
    "JSON_AS_ASCII": True,
    "JSON_SORT_KEYS": True,
    "JSONIFY_PRETTYPRINT_REGULAR": False,
    "JSONIFY_MIMETYPE": "application/json",
    "TEMPLATES_AUTO_RELOAD": None,
    "MAX_COOKIE_SIZE": 4093,
})
url_rule_class = Rule
url_map_class = Map
test_client_class = None
test_cli_runner_class = None
session_interface = SecureCookieSessionInterface()
import_name = None
template_folder = None
root_path = None
```

## app.py のコンストラクタ

引数とデフォルト値

- import_name,
- static_url_path=None
- static_folder="static"
- static_host=None
- host_matching=False
- subdomain_matching=False
- template_folder="templates"
- instance_path=None
- instance_relative_config=False
- root_path=None

instance_path に何も渡されていないときは、`auto_find_instans_path()`メソッドが呼び出される
instance_path に渡されたパスが存在しなければ ValueError 例外を返す

```python
self.instance_path = instance_path
self.config = self.make_config(instance_relative_config)
self.url_build_error_handlers = []
self.before_first_request_funcs = []
self.teardown_appcontext_funcs = []
self.shell_context_processors = []
self.blueprints = {}
self._blueprint_order = []
self.extensions = {}
self.url_map = self.url_map_class()
self.url_map.host_matching = host_matching
self.subdomain_matching = subdomain_matching
self._got_first_request = False
self._before_request_lock = Lock()
if self.has_static_folder:
    assert (
        bool(static_host) == host_matching
    ), "Invalid static_host/host_matching combination"
    self.add_url_rule(
        f"{self.static_url_path}/<path:filename>",
        endpoint="static",
        host=static_host,
        view_func=self.send_static_file,
    )
self.cli.name = self.
```

## プロパティ

- name
  `__main__`またはアプリケーション名のパッケージをインポートする
- propagate_exceptions
- preserve_context_on_exception
- logger
- jinja_env
- got_first_request
- templates_auto_reload
  setter で値が渡されていなければデバッグモードが有効になる
- debug

## メソッド

- make_config
- auto_find_instance_path
- open_instance_resource
- create_jinja_environment
- create_global_jinja_loader
- select_jinja_autoscape
- update_template_context
- make_shell_context
- run
- test_client
- test_cli_runner
- \_find_error_handler
- handle_http_exception
- trap_http_exception
- handle_user_exception
- handle_exception
- log_exception
- raise_routing_exception
- dispatch_request
- full_dispatch_request
- finalize_request
- try_trigger_before_first_request_function
- make_default_options_response
- should_ignore_error
- make_response
- create_url_adapter
- inject_url_defaults
- handle_url_build_error
- preprocess_request
- process_response
- do_teardown_requst
- do_teardown_appcontext
- app_context
- request_context
- test_request_context
- wsgi_app

## セットアップメソッド(デコレータ)

@setupmethod デコレータを実装しているのは scaffold.py(app.py が継承しているクラスに記載されている)

- register_bluprint
- add_url_rule
  - scaffold クラスでも機能は実装されていないもののメソッドは用意されている。
  - add_url_rule は scaffold の route メソッド内で decorator 関数でも使用されている。
  - route デコレータを通した関数は、route の decorator 関数内で呼ばれる add_url_rule 関数の view_func 引数に渡される
- template_filter
- add_template_filter
- template_test
- add_template_test
- template_global
- add_template_global
- before_first_request
- teardown_appcontext
- shell_context_processor

## マジックメソッド

- `__call__`
- `__repr__`

# blueprints.py

## Blueprint ヒアドキュメント

Represents a blueprint, a collection of routes and other app-related functions that can be registered on a real application later.

A blueprint is an object that allows defining application functions without requiring an application object ahead of time.
It uses the same decorators as :class:`~flask.Flask`, but defers the need for an application by recording them for later registration.

Decorating a function with a blueprint creates a deferred function that is called with :class:`~flask.blueprints.BlueprintSetupState` when the blueprint is registered on an application.

See :doc:`/blueprints` for more information.

## Blueprint ヒアドキュメント(jp)

実際のアプリケーションに後から登録できるルート設定や他のアプリ関連の機能などの集合であるブループリントを表しています。
ブループリントとは、あらかじめアプリケーションオブジェクトを必要とせずにアプリケーション機能を定義できるようにするためのオブジェクトです。
:class:`~flask.Flask` と同じデコレータを使いますが、後から登録するために記録しておくことで、アプリケーションの必要性を先送りします。

詳細は :doc:`/blueprints` を参照してください。

## メンバー変数

- warn_on_modifications = False
- \_got_registered_once = False
- json_encoder = None
- json_decoder = None
- import_name = None
- template_folder = None
- root_path = None

## メソッド

- \_is_setup_finished
- record

  - Registers a function that is called when the blueprint is registered on the application. This function is called with the state as argument as returned by the :meth:`make_setup_state` method.
  - ブループリントがアプリケーションで登録されたときに呼び出される関数を登録する。この関数は:meth:`make_setup_state`メソッドが返すステートを引数として呼び出される。

- record_once
- make_setup_state

  - Creates an instance of :meth:`~flask.blueprints.BlueprintSetupState` object that is later passed to the register callback functions. Subclasses can override this to return a subclass of the setup state.
  - レジスタコールバック関数に渡される:meth:`~flask.blueprints.BlueprintSetupState`のインスタンスを生成する。サブクラスは、これをオーバライドしてセットアップ状態のサブクラスを返すことができる。

- register
  - Called by :meth:`Flask.register_blueprint` to register all views and callbacks registered on the blueprint with the application. Creates a :class:`.BlueprintSetupState` and calls each :meth:`record` callback with it.
  - :meth:`Flask.register_blueprint` によって呼び出され、ブループリントに登録された全てのビューとコールバックをアプリケーションに登録します。:class:`.BlueprintSetupState` を作成し、それを使って各 :meth:`record` コールバックを呼び出します。
- add_url_rule
  - Like :meth:`Flask.add_url_rule` but for a blueprint. The endpoint for the :func:`url_for` function is prefixed with the name of the blueprint.
  - :meth:`Flask.add_url_rule`と似ていますが、ブループリント用です。:func:`url_for`関数用のエンドポイントには、ブループチンのプリフィックスが付けられます。
- app_template_filter
  - Register a custom template filter, available application wide. Like :meth:`Flask.template_filter` but for a blueprint.
  - カスタムテンプレートフィルタを登録します。:meth:`Flask.template_filter`のようなものですが、ブループリント用です。
- add_app_template_filter
- app_template_test
- add_app_template_test
- app_template_global
  - Register a custom template global, available application wide. Like :meth:`Flask.template_global` but for a blueprint.
- add_app_template_global
- before_app_request
- before_app_first_request
- after_app_request
- teardown_app_request
- app_context_processor
- app_errorhandler
- app_url_value_preprocessor
- app_url_defaults
