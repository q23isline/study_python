"""データベース例外エラー"""


class DatabaseError(Exception):
    """データベース例外エラー"""

    def __init__(self, message: str, code: int = 500) -> None:
        """
        :param message: str エラーメッセージ
        :param code: int エラーコード
        """
        super().__init__(message)
        self.code = code

    def __str__(self) -> str:
        """
        :return str
        """
        if self.code is not None:
            return f"[Error {self.code}] {super().__str__()}"
        return super().__str__()
