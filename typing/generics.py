from typing import Mapping, Sequence, TypeVar, Generic
from logging import Logger

"""
コンテナ(複数のオフジェクトを格納できるデータ構造)内のオブジェクトについての型情報は、
一般的な方法では静的型推論ができない。
そのため、抽象基底クラス(ABC)を継承したクラス(Mapping, Sequence等)を利用して、
コンテナ内オブジェクトの型を添え字表記でサポートするようになった。
"""


class Employee(object):
    pass


def notify_by_email(
    employees: Sequence[Employee], overrides: Mapping[str, str]
) -> None:
    pass


"""
TypeVar(型変数)を使って要素内の型も、任意の型として型推論させることができる。
"""

T = TypeVar("T")


def first(seq: Sequence[T]) -> T:
    return seq[0]


"""
ユーザ定義のクラスをジェネリッククラスとして定義する場合。
Generic[T]を基底クラスにすることで、型引数Tをとるクラスと定義することができる。
これによりクラスの中でもTが型として有効になる。
"""


class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log("set " + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log("Get " + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info("%s: %s", self.name, message)


"""
ジェネリック型は任意の数の型変数をとることができる。
また、型変数に制約をつけることも可能
"""

S = TypeVar("S")
U = TypeVar("U", int, str)


class StrangePair(Generic[T, S]):
    pass
