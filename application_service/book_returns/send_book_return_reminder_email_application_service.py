from datetime import datetime
from domain.models.book_rental.i_book_rental_repository import IBookRentalRepository
from domain.models.shared.mail.i_mail_client import IMailClient
from domain.models.shared.mail.message import Message
from domain.models.shared.mail.title import Title
from domain.models.shared.mail.mail import Mail


class SendBookReturnReminderEmailApplicationService:
    def __init__(self, r: IBookRentalRepository, c: IMailClient):
        self._r = r  # 本の貸出返却テーブルを操作
        self._c = c  # メール

    # メイン部
    def handle(self):
        # 催促対象者取得
        genzainichiji = datetime.now()
        u = self._r.get_users_with_unreturned_books_and_not_remind(genzainichiji)

        # 催促対象者にメール送信
        if len(u) > 0:
            for value in u:
                self._r.update_reminder_completed(value.user_id)
                self.handle2(value.user_id, value.mail_address)

        return len(u)

    def handle2(self, id, addr):
        self._r.update_reminder_completed(id)
        msg = Message(Message.BOOK_RETURN_REMINDER_EMAIL_CONTENT)
        # メールを m に格納する
        m = Mail(addr, Title(Title.BOOK_RETURN_REMINDER_EMAIL_TITLE), msg)
        self._c.send(m)
