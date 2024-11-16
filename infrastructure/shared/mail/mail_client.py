"""メール実装クラス"""

from domain.models.shared.mail.i_mail_client import IMailClient
from domain.models.shared.mail.mail import Mail


class MailClient(IMailClient):
    """メール実装クラス"""

    def send(self, mail: Mail) -> None:
        # 実装省略
        pass
