"""メールメッセージ"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    """
    メールメッセージ

    :param value: str メールメッセージ
    """

    value: str

    BOOK_RETURN_REMINDER_EMAIL_CONTENT = (
        "さん<br><br>このメールは、図書館からの自動送信メールです。<br>...（略）"
    )
