from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Неверная почта или пароль"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Токен истек"


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Токен отсутствует"


class IncorrectTokenFormat(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Неверный формат токена"


class UserFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Ошибка формата пользователя"


class RoomCannotBooked(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Не осталось свободных номеров"