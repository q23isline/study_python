"""メールタイトル"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Title:
    """
    メールタイトル

    :param value: str メールタイトル
    """

    value: str

    BOOK_RETURN_REMINDER_EMAIL_TITLE = "図書の返却期限が過ぎています"
