"""本の貸出返却管理データベースを操作する実装クラス"""

from datetime import datetime
from domain.models.book_rental.i_book_rental_repository import IBookRentalRepository
from domain.models.user.type.mail_address import MailAddress
from domain.models.user.type.user_id import UserId
from domain.models.user.user_collection import UserCollection
from domain.models.user.user import User

# from domain.models.shared.exception.database_error import DatabaseError


class BookRentalRepository(IBookRentalRepository):
    """本の貸出返却管理データベースを操作する実装クラス"""

    def get_users_with_unreturned_books_and_not_remind(
        self, deadline: datetime
    ) -> UserCollection:
        # データベースにアクセスして取得してきたテイ
        records = [
            {
                "id": "1",
                "mail_address": "sample1@example.com",
            },
            # {
            #     "id": "2",
            #     "mail_address": "sample2@example.com",
            # },
            # {
            #     "id": "3",
            #     "mail_address": "sample3@example.com",
            # },
        ]

        # データベースにアクセスして例外エラーが発生するテイ
        # raise DatabaseError("Failed to connect to the database", code=500)

        users = UserCollection()
        for record in records:
            users.add(User(UserId(record["id"]), MailAddress(record["mail_address"])))

        return users

    def update_reminder_completed(self, user_id: UserId) -> None:
        # 実装省略
        pass
