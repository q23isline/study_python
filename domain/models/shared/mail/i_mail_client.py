"""メールインターフェース"""

from abc import ABC, abstractmethod

from domain.models.shared.mail.mail import Mail


class IMailClient(ABC):
    """メールインターフェース"""

    @abstractmethod
    def send(self, mail: Mail) -> None:
        """
        送信する

        :param mail: Mail メール情報
        """
