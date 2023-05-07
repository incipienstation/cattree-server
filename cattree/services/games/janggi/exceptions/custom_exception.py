class CustomException(Exception):
    def __init__(self, message: str):
        self.__message = message + "\n"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__message}"
