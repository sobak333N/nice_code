from fastapi.exceptions import HTTPException


class MyException(Exception):
    def __init__(self, message: str="Instance doesn't exist", **kwargs):
        self.message = message
        super().__init__(self.message)


def main():
    # exc = MyException(message="This doesn't exist")
    exc = MyException()
    # print(exc.__dict__)
    raise exc


main()