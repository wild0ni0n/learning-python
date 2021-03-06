# Effective Python

## Python 流思考(Pythonic Thinking)

1. 使っている Python のバージョンを知っておく
2. PEP8 スタイルガイドに従う
3. bytes, str,unicode の違いを知っておく
4. 複雑な式の代わりにヘルパー関数を書く
5. シーケンスをどのようにスライスするか知っておく
6. 1 つのスライスでは、start, end, stride を使わない
7. map や filter の代わりにリスト内包表記を使う
8. リスト内包表記には、3 つ以上の式を避ける
9. 大きな内包表記にはジェネレータ式を考える
10. range よりは enumerate にする
11. iterator を並列に処理するには zip を使う
12. for と while ループの後の else ブロックは使うのを避ける
13. try/except/else/finally の書くブロックを活用する

## 関数

14. None を返すよりは例外を選ぶ
15. クロージャが変数スコープとどう関わるかを知っておく
16. リストを返さずにジェネレータを返すことを考える
17. 引数に対してイテレータを使うときには確実さを尊ぶ
18. 可変長位置引数を使って、見た目をすっきりさせる
19. キーワード引数にオプションの振る舞いを与える
20. 動的なデフォルト引数を指定するときには None とドキュメンテーション文字列を使う
21. キーワード専用引数で明確さを高める

## クラスと継承

22. 辞書やタプルで記録管理するよりもヘルパークラスを使う
23. 単純なインタフェースにはクラスの代わりに関数を使う
24. @classmethod ポリモルフィズムを使ってオブジェクトをジェネリックに構築する
25. 親クラスを super を使って初期化する
26. 多重継承は mix-in ユーティリティクラスだけに使う
27. プライベート属性よりはパブリック属性が好ましい
28. カスタムコンテナ型は collections.abc を継承する

## メタクラスと属性

29. get や set メソッドよりも素のままの属性を使う
30. 属性をリファクタリングする代わりに@property を考える
31. 再利用可能な@property メソッドにディスクリプタを使う
32. 遅延属性には`__getattr__`, `__getattribute__`, `__setattr__`を使う
33. サブクラスをメタクラスで検証する
34. クラスの存在をメタクラスで登録する
35. クラス属性をメタクラスで注釈する

## 並行性と並列性

36. subprocess を使って子プロセスを管理する
37. スレッドはブロッキング I/O に使い、並列性に使うのは避ける
38. スレッドでのデータ競合を防ぐために Lock を使う
39. スレッド間の協調作業には Queue を使う
40. 多くの関数を並行に実行するにはコルーチンを考える
41. 本当の並列性のために concurrent.futures を考える

## 組み込みモジュール

42. functools.wraps を使って関数デコレータを定義する
43. contextlib と with 文を try/finally の変わりに考える
44. copyreg で pickle を信頼できるようにする
45. ローカルクロックには time ではなく datetime を使う
46. 組み込みアルゴリズムとデータ構造を使う
47. 精度が特に重要な場合は decimal を使う
48. コミュニティ作成モジュールをどこで見つけられるかを知っておく

## 協働作業(コラボレーション)

49. 全ての関数、クラス、モジュールについてドキュメンテーション文字列を書く
50. モジュールの機会にパッケージを用い、安定な API を提供する
51. API からの呼び出し元を隔離するために、ルート例外を定義する
52. 循環依存をどのようにして止めるか知っておく
53. 隔離された複製可能な依存関係のために仮想環境を使う

## 本番運用準備

54. 本番環境を構築するのにモジュールスコープのコードを考える
55. 出力のデバッグには、repr 文字列を使う
56. unittest で全てをテストする
57. pdb で対話的にデバッグすることを考える
58. 最適化の前にプロファイル
59. メモリの仕様とリークを理解するたには tracemalloc を使う
