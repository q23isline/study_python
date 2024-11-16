"""メール情報"""

from __future__ import annotations
from dataclasses import dataclass
from domain.models.shared.mail.message import Message
from domain.models.shared.mail.title import Title
from domain.models.user.type.mail_address import MailAddress


@dataclass(frozen=True)
class Mail:
    """
    メール情報

    :param to_mail_address: UserId 送信先のメールアドレス
    :param message: Message メールメッセージ
    :param title: Title メールタイトル
    """

    to_mail_address: MailAddress
    title: Title
    message: Message
