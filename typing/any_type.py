from typing import Any

"""
静的型検査器は、すべての型をAnyと互換があるものとして扱い、Anyをすべての型と互換があるものとして扱う。
ただし、型エイリアスでAny型と定義した変数は、より詳細な型検査が行われない。
"""


def foo(item: Any) -> int:
    return item.bar()


"""
似たようなものとしてobjectがある。すべての型はobjectと互換があるものとして扱われるが、
objectは全ての型と互換があるわけではない（サブタイプではない）

objectは、ある値が型安全な方法で任意の型として使えることを示すために使用します。
Any はある値が動的に型付けられることを示すために使用します。
"""


def hash_a(item: object) -> int:
    return item.magic()  # "object" has no attribute "magic"mypy(error)


def hash_b(item: Any) -> int:
    return item.magic()  # OK
