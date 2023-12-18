from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("token", "id", "name", "email")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    token: str
    id: int
    name: str
    email: str
    def __init__(self, token: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ("name", "email", "password")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    email: str
    password: str
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("id", "name", "email")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("token", "name", "email", "password")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    token: str
    name: str
    email: str
    password: str
    def __init__(self, token: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("id", "name", "email")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
