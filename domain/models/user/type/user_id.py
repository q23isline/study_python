"""ユーザーID"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    """
    ユーザーID

    :param value: str ユーザーID
    """

    value: str
