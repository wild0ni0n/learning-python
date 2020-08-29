from typing import NewType

UserId = NewType("UserId", int)
some_id = UserId(12345)
print(type(some_id))  # <class 'int'>


def get_user_name(user_id: UserId) -> str:
    return "Bob" if user_id == 12345 else "Unknown"


user_a = get_user_name(UserId(12345))

user_b = get_user_name(-1)  # mypy error
