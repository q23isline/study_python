"""ユーザー一覧"""

from collections.abc import Iterable
from typing import Iterator
from domain.models.user.user import User


class UserCollection(Iterable):
    """ユーザー一覧"""

    def __init__(self) -> None:
        self._attributes: list[User] = []

    def add(self, user: User) -> None:
        """
        ユーザーを一覧に追加する

        :param user: User ユーザー
        """
        self._attributes.append(user)

    def __len__(self) -> int:
        """
        ユーザー数を返す

        :return: int
        """
        return len(self._attributes)

    def __iter__(self) -> Iterator[User]:
        """
        ユーザー一覧を for ループで取得できるようにする

        :return: Iterator[User]
        """
        return iter(self._attributes)
