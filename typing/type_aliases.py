from typing import List, Dict, Tuple, Sequence

# 型エイリアス サンプル
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


new_vector = scale(2.0, [1.0, -4.2, 5.4])

# -----------
# 複雑な型シグネチャを単純化するのに有用な例

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

# def broadcast_message(message: str, servers: Sequence[Server]) -> None:
#    pass


def broadcast_message(
    message: str, servers: Sequence[Tuple[Tuple[str, int], Dict[str, str]]]
) -> None:
    pass
