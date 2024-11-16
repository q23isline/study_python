"""本の貸出返却管理データベースを操作するインターフェース"""

from abc import ABC, abstractmethod
from datetime import datetime

from domain.models.user.type.user_id import UserId
from domain.models.user.user_collection import UserCollection


class IBookRentalRepository(ABC):
    """本の貸出返却管理データベースを操作するインターフェース"""

    @abstractmethod
    def get_users_with_unreturned_books_and_not_remind(
        self, deadline: datetime
    ) -> UserCollection:
        """
        未催促で本が未返却のユーザーを取得する

        :param deadline: datetime 返却期限日
        :return: UserCollection
        :raises: DatabaseError
        """

    @abstractmethod
    def update_reminder_completed(self, user_id: UserId) -> None:
        """
        催促済のユーザーとして更新する

        :param user_id: UserId 更新対象のユーザーID
        :return: None
        :raises: DatabaseError
        """
