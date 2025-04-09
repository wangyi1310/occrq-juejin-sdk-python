class JuejinAPIError(Exception):
    """Juejin API exception"""

    def __init__(self, message: str, code: int):
        """
        Initialize the exception

        Parameters:
            message: Error message
            code: Error code
        """
        self.message = message
        self.code = code
        super().__init__(f"[{code}] {message}")

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"