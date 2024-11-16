"""書籍返却催促メールのメイン処理"""

from datetime import datetime
from domain.models.book_rental.i_book_rental_repository import IBookRentalRepository
from domain.models.shared.mail.i_mail_client import IMailClient
from domain.models.shared.mail.message import Message
from domain.models.shared.mail.title import Title
from domain.models.shared.mail.mail import Mail
from domain.models.user.type.mail_address import MailAddress
from domain.models.user.user_collection import UserCollection


class SendBookReturnReminderEmailApplicationService:
    """書籍返却催促メールのメイン処理"""

    def __init__(
        self,
        book_rental_repository: IBookRentalRepository,
        mail_client: IMailClient,
    ) -> None:
        """
        :param book_rental_repository: IBookRentalRepository 本の貸出返却テーブルを操作
        :param mail_client: IMailClient メール
        """
        self._book_rental_repository = book_rental_repository
        self._mail_client = mail_client

    def handle(self) -> int:
        """
        メイン処理

        :return: int メール送信人数
        :raises DatabaseError
        """
        # 催促対象者取得
        users = (
            self._book_rental_repository.get_users_with_unreturned_books_and_not_remind(
                datetime.now()
            )
        )

        if len(users) == 0:
            return 0

        # 催促対象者にメール送信
        self.__send_users_with_reminder(users)

        return len(users)

    def __send_users_with_reminder(self, users: UserCollection) -> None:
        """
        催促済に更新してメール送信する

        :param users: UserCollection ユーザー一覧
        :return: None
        :raises DatabaseError
        """
        for user in users:
            self._book_rental_repository.update_reminder_completed(user.user_id)
            self.__send_mail(user.mail_address)

    def __send_mail(self, to_mail_address: MailAddress) -> None:
        """
        メールを送信する

        :param to_mail_address: MailAddress 送信先メールアドレス
        :return: None
        """
        title = Title(Title.BOOK_RETURN_REMINDER_EMAIL_TITLE)
        message = Message(Message.BOOK_RETURN_REMINDER_EMAIL_CONTENT)
        mail = Mail(to_mail_address, title, message)
        self._mail_client.send(mail)
