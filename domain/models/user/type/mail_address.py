"""メールアドレス"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class MailAddress:
    """
    メールアドレス

    :param value: str メールアドレス
    """

    value: str
