from typing import Callable

# コールバック関数を要求する場合、Callable[[Arg1Type, Arg2Type], ReturnType]を使って型ヒントを指定することができる。


def feeder(get_next_item: Callable[[], str]) -> None:
    pass


def async_query(
    on_success: Callable[[int], None], on_error: Callable[[int, Exception], None]
) -> None:
    pass
