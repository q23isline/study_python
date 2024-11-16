"""自動通知機能バッチ"""

from application_service.book_returns.send_book_return_reminder_email_application_service import (
    SendBookReturnReminderEmailApplicationService,
)
from infrastructure.book_rentals.book_rental_repository import BookRentalRepository
from infrastructure.shared.mail.mail_client import MailClient
from domain.models.shared.exception.database_error import DatabaseError


def main() -> None:
    """自動通知機能バッチ"""

    # 開始部
    print("－－－－－書籍返却催促メール送信処理 を開始します－－－－－")

    # メイン部
    service = SendBookReturnReminderEmailApplicationService(
        BookRentalRepository(),
        MailClient(),
    )

    try:
        result = service.handle()
    except DatabaseError:
        print(
            "－－－－－データベースにアクセスできませんでした。異常終了します－－－－－"
        )
        return

    # 終了部
    print(f"{result} 人に書籍返却催促メールを送信しました。")
    print("－－－－－書籍返却催促メール送信処理 を終了します－－－－－")


if __name__ == "__main__":
    main()
