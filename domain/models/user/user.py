"""ユーザー"""

from __future__ import annotations
from dataclasses import dataclass
from domain.models.user.type.user_id import UserId
from domain.models.user.type.mail_address import MailAddress


@dataclass(frozen=True)
class User:
    """
    ユーザー

    :param user_id: UserId ユーザーID
    :param mail_address: MailAddress メールアドレス
    """

    user_id: UserId
    mail_address: MailAddress
